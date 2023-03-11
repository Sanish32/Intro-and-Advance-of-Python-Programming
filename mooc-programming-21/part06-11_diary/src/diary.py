# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    fun=int(input("Function:"))
    if fun==1:
        entry=input("Diary entry:")
        with open("diary.txt","a") as file:
            file.write(f"{entry}\n")
        print("Diary saved\n")
    elif fun==2:
        print("Entries:")
        with open("diary.txt") as file:
            for line in file:
                line=line.replace("\n","")
                print(line)
    elif fun==0:
        print("Bye now!")
        break