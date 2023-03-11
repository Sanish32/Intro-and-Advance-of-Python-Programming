dict1={}
def exer(exe):
    with open(exe) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            if words[0]=="id":
                continue
            total=0
            for items in words[1:]:
                total+=int(items)
            dict1[words[0]]=total
dict2={}
def stud(stu):
    with open(stu) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            if words[0]=="id":
                continue
            dict2[words[0]]=f"{words[1]} {words[2]}"
x=input("Student information:")
stud(x)  
y=input("Exercises completed:")
exer(y)
for id,name in dict2.items():
    if id in dict1:
        print(f"{name} {dict1[id]}")