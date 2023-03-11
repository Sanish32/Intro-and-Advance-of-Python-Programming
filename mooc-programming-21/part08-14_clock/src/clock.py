# Write your solution here:
class Clock:
    def __init__(self,hours:int,minutes:int,seconds:int):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        

    def tick(self):
        if self.seconds<60:
            self.seconds+=1
        if self.seconds==60:
            self.minutes+=1
            self.seconds=0
        if self.minutes==60:
            self.hours+=1
            self.minutes=0
            self.seconds=0
        if self.hours==24:
            self.hours=0
            self.minutes=0
            self.seconds=0

    def set(self,hour=0,minute=0,second=0):
        self.hours=hour
        self.minutes=minute
        self.seconds=second

if __name__=="__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)