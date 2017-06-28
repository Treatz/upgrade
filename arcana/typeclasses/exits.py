from typeclasses.myslow_exit import myCmdSetSpeed, mySlowExit
from evennia.commands import command
from evennia.commands import cmdset

class Exit(mySlowExit):
    def can_traverse(self, character):
        if character.db.conscious == 0:
            character.msg("You are unconscious and cannot move.")
            return
        if self.access(character, 'traverse'):
            # we may traverse the exit.
            return True
        elif character.db.bypass_locked_doors:
            msg = character.db.bypass_locked_doors or "You ignore the locked door."
            character.msg(msg)
            return True
        else:
            # exit is locked
            if self.db.err_traverse:
                # if exit has a better error message, let's use it.
                character.msg(self.db.err_traverse)
            else:
                # No shorthand error message. Call hook.
                self.at_failed_traverse(character)

    def create_exit_cmdset(self, exidbobj):
        """
        Helper function for creating an exit command set + command.

        The command of this cmdset has the same name as the Exit object
        and allows the exit to react when the player enter the exit's name,
        triggering the movement between rooms.

        Note that exitdbobj is an ObjectDB instance. This is necessary
        for handling reloads and avoid tracebacks if this is called while
        the typeclass system is rebooting.
        """
        exitkey = exidbobj.db_key.strip().lower()
        exitaliases = list(exidbobj.aliases.all())

        # noinspection PyUnresolvedReferences
        class ExitCommand(command.Command):
            """
            This is a command that simply cause the caller
            to traverse the object it is attached to.
            """
            obj = None

            def func(self):
                """Default exit traverse if no syscommand is defined."""
                if self.obj.can_traverse(self.caller):
                    self.obj.at_traverse(self.caller, self.obj.destination)

        # noinspection PyUnresolvedReferences
        class PassExit(command.Command):
            def func(self):
                if self.obj.db.locked and not self.obj.access(self.caller, 'usekey'):
                    self.caller.msg("You don't have a key to this exit.")
                    return
                self.obj.at_traverse(self.caller, self.obj.destination)

        # noinspection PyUnresolvedReferences
        class KnockExit(command.Command):
            def func(self):
                self.caller.msg("You knocked on the door.")
                self.obj.destination.msg_contents("{wThere is a knock coming from %s." % self.obj.reverse_exit)

        # create an exit command. We give the properties here,
        # to always trigger metaclass preparations
        exitcmd = ExitCommand(key=exitkey,
                              aliases=exitaliases,
                              locks=str(exidbobj.locks),
                              auto_help=False,
                              destination=exidbobj.db_destination,
                              arg_regex=r"$",
                              is_exit=True,
                              obj=exidbobj)

        # create a cmdset
        exit_cmdset = cmdset.CmdSet(None)
        exit_cmdset.key = '_exitset'
        exit_cmdset.priority = 101  # equal to channel priority
        exit_cmdset.duplicates = True
        # add command to cmdset
        exit_cmdset.add(exitcmd)
        # exit_cmdset.add(passcmd)
        # exit_cmdset.add(knockcmd)
        return exit_cmdset
        
    @property
    def reverse_exit(self):
        entrances = [ob for ob in self.destination.exits if ob.destination == self.location]
        if not entrances:
            return "nowhere"
        return entrances[0]

class CmdFaster(myCmdSetSpeed):

    key = "faster"

    def func(self):
        """
        Simply sets an Attribute used by the SlowExit above.
        """

        if self.caller.db.move_speed == "stroll":
            self.caller.db.move_speed = "walk"
        elif self.caller.db.move_speed == "walk":
            self.caller.db.move_speed = "run"
        elif self.caller.db.move_speed == "run":
            self.caller.db.move_speed = "sprint"

        self.caller.msg("You are now %sing." % self.caller.db.move_speed)

    pass

class CmdSlower(myCmdSetSpeed):

    key = "slower"

    def func(self):
        """
        Simply sets an Attribute used by the SlowExit above.
        """

        if self.caller.db.move_speed == "sprint":
            self.caller.db.move_speed = "run"
        elif self.caller.db.move_speed == "run":
            self.caller.db.move_speed = "walk"
        elif self.caller.db.move_speed == "walk":
            self.caller.db.move_speed = "stroll"

        self.caller.msg("You are now %sing." % self.caller.db.move_speed)

    pass
