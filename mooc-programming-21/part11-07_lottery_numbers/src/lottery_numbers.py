# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self,num,list):
        self.num=num
        self.abc=list

    def number_of_hits(self,items:list):
        return len([item for item in self.abc if item in items])

    def hits_in_place(self,items):
        return [item  if item in self.abc else -1 for item in items]

if __name__=="__main__":
    week5=LotteryNumbers(5,[1,2,3,4,5,6,7])
    my_numbers=[1,4,7,11,13,19,24]
    print(week5.hits_in_place(my_numbers))