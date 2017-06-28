from evennia.utils.evmenu import EvMenu
from evennia import DefaultScript
import time

class AttackTime(DefaultScript):

    def at_script_creation(self):
        self.key = "attackWait"
        self.desc = "Character loses a turn."
        self.interval = 2  # seconds
        self.repeats = 10  # repeat only a certain number of times
        self.start_delay = True  # wait self.interval until first call
        # self.persistent = True


    def at_repeat(self):
        """
        This gets called every self.interval seconds. We make
        a random check here so as to only return 33% of the time.
        """
        self.obj.db.current_time = time.time()
        timer = self.obj.db.current_time
        clock = self.obj.db.start_time
	if(self.obj.db.conscious == 0):
	    if (timer - clock) > 2:
                self.obj.execute_cmd("skip")
                self.obj.db.start_time = 99999999999999999
		self.stop()

        if(self.obj.db.conscious == 1):			
            if (timer - clock) > 12:
               self.obj.execute_cmd("skip")
               self.obj.db.start_time = 99999999999999999
               self.stop()
            elif(self.obj.db.target.has_player<1):
                self.obj.db.target.execute_cmd("skip")
                self.obj.db.start_time = 99999999999999999
                self.stop()



    def attacker(self, character):
        self.db.attacker = character

    def target(self, character):
        self.db.target = character
