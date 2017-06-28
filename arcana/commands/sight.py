from evennia.commands.default.muxcommand import MuxCommand


class CmdSight(MuxCommand):
   
    key = "+sight"
    locks = "cmd:all()"

    def func(self):
        self.caller.db.sight = 1
        self.caller.msg("You can now see into the spirit world.")
