import time

from dayCycle import DayCycle

if __name__ == "__main__":
    print("Hello World")

i = DayCycle(5)

i.increase_time()
i.increase_time()

print(i.time_of_day())