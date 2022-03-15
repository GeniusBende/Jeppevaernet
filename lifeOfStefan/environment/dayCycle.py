class DayCycle:
    time = 0

    def __init__(self, time):
        if (time < 0 or time > 23):
            self.time = 0
        else:
            self.time = time

    def time_of_day(self):
        return self.time

    def increase_time(self):
        if (self.time == 23):
            self.time = 0
        else:
            self.time += 1

