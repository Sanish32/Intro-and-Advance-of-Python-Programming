# Write your solution here
dictionary={}
while True:
    num=int(input("command (1 search, 2 add, 3 quit):"))
    if num==1:
        name=input("name:")
        if name in dictionary:
            for i in range(len(dictionary[name])):
                print(f"{dictionary[name][i]}")
        else:
            print("no number")
    elif num==2:
        name=input("name:")
        phone=input("number:")
        if name not in dictionary:
            dictionary[name]=[]
        dictionary[name].append(phone)
        print("ok!")
    else: 
        print("quitting...")
        break
