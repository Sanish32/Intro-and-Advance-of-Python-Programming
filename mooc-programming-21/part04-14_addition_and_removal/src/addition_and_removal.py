# Write your solution here
list=[]
print("The list is now []")
i=1
while True:
    choose=input("a(d)d, (r)emove or e(X)it:")
    if choose == "x":
        break
    elif choose =="d":
        list.append(i)
        i+=1
    else:
        list.pop(i-2)
        i-=1
    print(f"The list is now {list}")
print("Bye!")