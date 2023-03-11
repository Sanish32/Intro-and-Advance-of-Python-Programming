# Write your solution here
from random import choice
def roll(die:str):
    if die=="A":
        x=choice([3,3,3,3,3,6])
    elif die=="B":
        x=choice([2,2,2,5,5,5])
    elif die=="C":
        x=choice([1,4,4,4,4,4])
    return x

def play(die1,die2,times):
    c=0
    d=0
    e=0
    for i in range(times):
        if die1=="A":
            x=choice([3,3,3,3,3,6])
        elif die1=="B":
            x=choice([2,2,2,5,5,5])
        elif die1=="C":
            x=choice([1,4,4,4,4,4])
        if die2=="A":
            y=choice([3,3,3,3,3,6])
        elif die2=="B":
            y=choice([2,2,2,5,5,5])
        elif die2=="C":
            y=choice([1,4,4,4,4,4])
        if x>y:
            c+=1
        elif x<y:
            d+=1
        else:
            e+=1
    return c,d,e
if __name__=="__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)