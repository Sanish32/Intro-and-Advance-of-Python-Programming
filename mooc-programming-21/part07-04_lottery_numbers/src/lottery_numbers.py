# Write your solution here
from random import randint
def lottery_numbers(amount:int,lower:int,upper:int):
    new=[]
    i=0
    while i<amount:
        new.append(randint(lower,upper))
        i+=1
    new.sort()
    print(new)
    i=1
    need=len(new)
    count=len(new)
    while i<len(new):
        if new[i-1]==new[i]:
            new.remove(new[i])
            count-=1
        i+=1
    i=0
    if need!=count:
        while i<(need-count):
            new.append(randint(lower,upper))
            i+=1
    new.sort()
    return new 
if __name__=="__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)