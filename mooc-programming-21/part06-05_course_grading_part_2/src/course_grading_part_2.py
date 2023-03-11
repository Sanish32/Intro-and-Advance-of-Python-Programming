# write your solution here
dict1={}
def stud(stu):
    with open(stu) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            if words[0]=="id":
                continue
            dict1[words[0]]=f"{words[1]} {words[2]}"
dict2={}
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
            dict2[words[0]]=total
dict3={}
def exam(z):
    with open(z) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            if words[0]=="id":
                continue
            total=0
            for items in words[1:]:
                total+=int(items)
            dict3[words[0]]=total
x=input("Student information:")
stud(x)  
y=input("Exercises completed:")
exer(y)
z=input("Exam points:")
exam(z)
for id,name in dict1.items():
    if id in dict2 and id in dict3:
        j=10
        for i in range(40,4,-4):
            if dict2[id]==0:
                points=0
                break
            elif dict2[id]>i-1:
                points=j
                break
            j-=1
        abc=dict3[id]+points
        
        if abc>=27:
                g=5
        elif abc>23:
            g=4
        elif abc>20:
            g=3
        elif abc>17:
            g=2
        elif abc>14:
            g=1
        else:
            g=0
    print(f"{name} {g}")