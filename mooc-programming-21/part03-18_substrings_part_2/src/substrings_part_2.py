# Write your solution here
string=input("Please type in a string:")
num=-1
length=len(string)*(-1)
while num >= length:
    print(string[num:])
    num-=1