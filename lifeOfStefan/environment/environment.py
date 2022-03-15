import time

from stefan.states import States

class Environment:

    person = None
    day = None

    def __init__(self, person, dayCycle):
        self.person = person
        self.day = dayCycle

    def start(self):
        while(True):
            print("\n" + str(self.day.time_of_day()) + ":00")

            if (self.day.time_of_day() < 24 and self.day.time_of_day() > 7):
                if (self.person.get_state() is States.AWAKE):
                    self.person.masturbate()
                elif (self.person.get_state() is States.TIRED):
                    if (self.person.has_coffee()):
                        self.person.drink_coffee()
                    else:
                        self.person.make_coffee()
                else:
                    if (self.person.power_level() > 7):
                        self.person.wake_up()
                    else:
                        self.person.sleep()
            else:
                if (self.person.is_awake()):
                    self.person.masturbate_furiously()
                else:
                    self.person.sleep()
            
            self.day.increase_time()
            time.sleep(1)