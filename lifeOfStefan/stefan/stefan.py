from stefan.states import States

class Stefan:
    power = 0
    state = States.SLEEPING
    coffee = False

    def __init__(self, power, state):
        self.power = power
        self.state = state

    def make_coffee(self):
        self.coffee = True
        print("Stefan makes coffee")

    def drink_coffee(self):
        if self.coffee is True:
            self.coffee = False
            self.power += 4
            self.set_state(States.AWAKE)
            print("Stefan drinks coffee")

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def use_power(self, used):
        if (self.power >= used):
            self.power -= used
            if (self.power < 3):
                self.state = States.TIRED
                print("Stefan is tired")
        else:
            self.power = 0
            self.set_state(States.SLEEPING)
            print("Stefan is now sleeping")

    def masturbate(self):
        print("Stefan masturbates")
        self.use_power(1)

    def masturbate_furiously(self):
        print("Stefan masturbate furiously")
        self.use_power(3)

    def sleep(self):
        print("Stefan is sleeping")
        self.power += 1

    def wake_up(self):
        print("Stefan wakes up")
        self.state = States.AWAKE

    def power_level(self):
        return self.power

    def is_awake(self):
        if self.state == States.SLEEPING:
            return False
        else:
            return True

    def has_coffee(self):
        if (self.coffee is True):
            return True
        else:
            return False

