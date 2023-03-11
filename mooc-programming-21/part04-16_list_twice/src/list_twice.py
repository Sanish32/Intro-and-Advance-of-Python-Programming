# Write your solution here
list=[]
while True:
    item=int(input("New item:"))
    if item==0:
        break
    else:
        list.append(item)
        print(f"The list now: {list}")
        new_list=sorted(list)
        print(f"The list in order: {new_list}")
print("Bye!")