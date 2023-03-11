# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
    list=[]
    for i in range(amount):
        list.append(Fraction(1,amount))
    return list
if __name__=="__main__":
    print(fractionate(5))