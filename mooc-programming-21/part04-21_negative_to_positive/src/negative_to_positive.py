# Write your solution here
num=int(input("Please type in a postive integer:"))
a=num*(-1)
for i in range(a,num+1,1):
    if i==0:
        continue
    if i!=0:
        print(i)