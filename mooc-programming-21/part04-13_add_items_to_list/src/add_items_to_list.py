# Write your solution here
list=[]
times=int(input("How many items:"))
i=1
a=0
while i <= times:
    a=int(input(f"Item {i}:"))
    list.append(a)
    i+=1
print(list)