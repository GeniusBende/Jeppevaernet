from environment.environment import Environment
from environment.dayCycle import DayCycle
from stefan.stefan import Stefan
from stefan.states import States

def main():
    person = Stefan(10, States.AWAKE)
    day = DayCycle(8)
    environment = Environment(person, day)

    environment.start()


if __name__ == "__main__":
    print("Hello World")
    main()

