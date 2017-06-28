from evennia.commands.default.muxcommand import MuxCommand


class CmdLastBreath(MuxCommand):
   
    key = "+lastbreath"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)
        if hit.db.lastname:
            self.caller.msg("They used to be named %s." % hit.db.lastname)
            self.caller.msg("The last person to attack %s was %s." % (hit.db.lastname, hit.db.target))
        else:
              self.caller.msg("The last person to attack %s was %s." % (hit, hit.db.target))
