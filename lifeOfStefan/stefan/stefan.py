from states import States

class Stefan:
    power = 0
    state = States.SLEEPING

    def __init__(self, power, state):
        self.power = power
        self.state = state

    def isAwake(self):
        return True

    