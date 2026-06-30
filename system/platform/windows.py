from enum import Enum

class Windows(object):
    def __init__(self):
        print("Windows:{0}".format(__name__))

    def windows(self):
        print("this is windows system")


class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


if __name__ == "__main__":
    w = Windows()
    w.windows()
    
    print(WeekDays.MONDAY)