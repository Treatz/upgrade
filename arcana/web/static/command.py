"""
Commands

Commands describe the input the player can do to the game.

"""
from evennia.commands.default.muxcommand import MuxCommand
from evennia import Command as BaseCommand
from evennia import default_cmds
from django.conf import settings
from evennia import Command, create_object, utils
from evennia.utils import create, utils
from evennia.commands.default import unloggedin
from evennia.utils import evform, evtable



# from evennia import default_cmds



class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_command(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_command(): Extra actions, often things done after
            every command, like prompts.

    """
    pass


# ------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# ------------------------------------------------------------

# from evennia.utils import utils
# class MuxCommand(Command):
#    """
#    This sets up the basis for a MUX command. The idea
#    is that most other Mux-related commands should just
#    inherit from this and don't have to implement much
#    parsing of their own unless they do something particularly
#    advanced.
#
#    Note that the class's __doc__ string (this text) is
#    used by Evennia to create the automatic help entry for
#    the command, so make sure to document consistently here.
#    """
#    def has_perm(self, srcobj):
#        """
#        This is called by the cmdhandler to determine
#        if srcobj is allowed to execute this command.
#        We just show it here for completeness - we
#        are satisfied using the default check in Command.
#        """
#        return super(MuxCommand, self).has_perm(srcobj)
#
#    def at_pre_cmd(self):
#        """
#        This hook is called before self.parse() on all commands
#        """
#        pass
#
#    def at_post_cmd(self):
#        """
#        This hook is called after the command has finished executing
#        (after self.func()).
#        """
#        pass
#
#    def parse(self):
#        """
#        This method is called by the cmdhandler once the command name
#        has been identified. It creates a new set of member variables
#        that can be later accessed from self.func() (see below)
#
#        The following variables are available for our use when entering this
#        method (from the command definition, and assigned on the fly by the
#        cmdhandler):
#           self.key - the name of this command ('look')
#           self.aliases - the aliases of this cmd ('l')
#           self.permissions - permission string for this command
#           self.help_category - overall category of command
#
#           self.caller - the object calling this command
#           self.cmdstring - the actual command name used to call this
#                            (this allows you to know which alias was used,
#                             for example)
#           self.args - the raw input; everything following self.cmdstring.
#           self.cmdset - the cmdset from which this command was picked. Not
#                         often used (useful for commands like 'help' or to
#                         list all available commands etc)
#           self.obj - the object on which this command was defined. It is often
#                         the same as self.caller.
#
#        A MUX command has the following possible syntax:
#
#          name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#        The 'name[ with several words]' part is already dealt with by the
#        cmdhandler at this point, and stored in self.cmdname (we don't use
#        it here). The rest of the command is stored in self.args, which can
#        start with the switch indicator /.
#
#        This parser breaks self.args into its constituents and stores them in the
#        following variables:
#          self.switches = [list of /switches (without the /)]
#          self.raw = This is the raw argument input, including switches
#          self.args = This is re-defined to be everything *except* the switches
#          self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                     no = is found, this is identical to self.args.
#          self.rhs: Everything to the right of = (rhs:'right-hand side').
#                    If no '=' is found, this is None.
#          self.lhslist - [self.lhs split into a list by comma]
#          self.rhslist - [list of self.rhs split into a list by comma]
#          self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#          All args and list members are stripped of excess whitespace around the
#          strings, but case is preserved.
#        """
#        raw = self.args
#        args = raw.strip()
#
#        # split out switches
#        switches = []
#        if args and len(args) > 1 and args[0] == "/":
#            # we have a switch, or a set of switches. These end with a space.
#            switches = args[1:].split(None, 1)
#            if len(switches) > 1:
#                switches, args = switches
#                switches = switches.split('/')
#            else:
#                args = ""
#                switches = switches[0].split('/')
#        arglist = [arg.strip() for arg in args.split()]
#
#        # check for arg1, arg2, ... = argA, argB, ... constructs
#        lhs, rhs = args, None
#        lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#        if args and '=' in args:
#            lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#            lhslist = [arg.strip() for arg in lhs.split(',')]
#            rhslist = [arg.strip() for arg in rhs.split(',')]
#
#        # save to object properties:
#        self.raw = raw
#        self.switches = switches
#        self.args = args.strip()
#        self.arglist = arglist
#        self.lhs = lhs
#        self.lhslist = lhslist
#        self.rhs = rhs
#        self.rhslist = rhslist
#
#        # if the class has the player_caller property set on itself, we make
#        # sure that self.caller is always the player if possible. We also create
#        # a special property "character" for the puppeted object, if any. This
#        # is convenient for commands defined on the Player only.
#        if hasattr(self, "player_caller") and self.player_caller:
#            if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                # caller is an Object/Character
#                self.character = self.caller
#                self.caller = self.caller.player
#            elif utils.inherits_from(self.caller, "evennia.players.players.DefaultPlayer"):
#                # caller was already a Player
#                self.character = self.caller.get_puppet(self.session)
#            else:
#                self.character = None
#


class FooBar(Command):
    key = "foobar"

    def func(self):
        foobar = create.create_player("TestPlayer4", email="test@test.com", password="testpassword",
                                      typeclass=settings.BASE_PLAYER_TYPECLASS)
        foobar.db.FIRST_LOGIN = True
        self.msg("%s" % foobar)
        unloggedin._create_character(self, foobar, settings.BASE_CHARACTER_TYPECLASS, settings.DEFAULT_HOME,
                                     settings.PERMISSION_PLAYER_DEFAULT)

class OverLook(default_cmds.CmdLook):
    key = "look"
    def func(self):
        if(self.caller.db.alive == 1 and self.caller.db.conscious == 1):
            super(OverLook, self).func()
        else:
            self.caller.msg("You can't see.")
class OverHome(default_cmds.CmdHome):
    key = "home"
    def func(self):
        if(self.caller.db.conscious  == 1):
		super(OverHome, self).func()
        else:
            self.caller.msg("You can't do that while unconscious")

class OverInventory(default_cmds.CmdInventory):
    key = "i"
    def func(self):
        if(self.caller.db.conscious == 1):
                self.caller.msg("test")
        else:
            self.caller.msg("You can't do that while unconscious")

class Kill(MuxCommand):
    key = "kill"
    lock = "cmd:all()"

    def func(self):
        if self.lhs:
            obj = self.caller.search(self.lhs)
            obj.db.alive = 0
            self.caller.msg("%s is dead." % (obj.key))


class Heal(MuxCommand):
    key = "heal"
    lock = "cmd:all()"

    def func(self):
        if self.lhs:
            obj = self.caller.search(self.lhs)
            obj.db.alive = 1
            obj.db.bashing = 0
            obj.db.lethal = 0
            self.caller.msg("%s is alive." % (obj.key))

class Wield(default_cmds.MuxCommand):
	key = "wield"

	def func(self):
		self.caller.db.selected_weapon = self.args
		self.caller.msg("|/|gYou wield %s" % self.args)



class Image(default_cmds.MuxCommand):
    """
    Face

    Usage:
      image [url]

    This command sets your character's image.
    """

    key = "image"

    def func(self):
        if not self.args:
            self.caller.msg("You didn't provide a url.")
        else:
            self.caller.db.image = self.args
            self.caller.msg("Image set.")

class Sheet(MuxCommand):

    key = "sheet"
    lock = "cmd:all()"

    def func(self):
        form = evform.EvForm("world/charactersheetform.py")
        form.map(cells={1: self.caller.name,
                        2: self.caller.db.tradition,
                        3: self.caller.db.essence,
                        4: self.caller.db.concept,
                        5: self.caller.db.desc,
                        6: self.caller.db.strength,
                        7: self.caller.db.dexterity,
                        8: self.caller.db.stamina,
                        9: self.caller.db.charisma,
                        10: self.caller.db.manipulation,
                        11: self.caller.db.appearance,
                        12: self.caller.db.perception,
                        13: self.caller.db.intelligence,
                        14: self.caller.db.wits,
                        15: self.caller.db.alertness,
                        16: self.caller.db.athletics,
                        17: self.caller.db.awareness,
                        18: self.caller.db.brawl,
                        19: self.caller.db.intimidation,
                        20: self.caller.db.streetwise,
                        21: self.caller.db.drive,
                        22: self.caller.db.firearms,
                        23: self.caller.db.martialarts,
                        24: self.caller.db.melee,
                        25: self.caller.db.meditation,
                        26: self.caller.db.stealth,
                        27: self.caller.db.astrology,
                        28: self.caller.db.computer,
                        29: self.caller.db.language,
                        30: self.caller.db.medicine,
                        31: self.caller.db.occult,
                        32: self.caller.db.rituals,
                        33: self.caller.db.correspondence,
                        34: self.caller.db.entropy,
                        35: self.caller.db.forces,
                        36: self.caller.db.life,
                        37: self.caller.db.matter,
                        38: self.caller.db.mind,
                        39: self.caller.db.prime,
                        40: self.caller.db.spirit,
                        41: self.caller.db.time,
                        42: self.caller.db.arete,
                        43: self.caller.db.arcane,
                        44: self.caller.db.avatar,
                        45: self.caller.db.willpower,
                        46: self.caller.db.belief,
                        47: self.caller.db.familiar,
                        48: self.caller.db.quitnessence,
                        49: self.caller.db.luck,
                        50: self.caller.db.resources})

        self.caller.msg(unicode(form))

