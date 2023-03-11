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
word1="name"
word2="exec_nbr"
word3="exec_pts."
word4="exm_pts."
word5="tot_pts."
word6="grade"
v=input("Course Text")
with open("results.txt","w") as my_file:
    new=[]
    with open(v) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(":")
            if words[0]!="name" or words[0]!="studycredits":
                new.append(words[1])
    my_file.write(f"{new[0]},{new[1]} credits\n")
    my_file.write("======================================\n")
    my_file.write(f"{word1:30}{word2:<10}{word3:<10}{word4:<10}{word5:<10}{word6}\n")
    with open("results.csv","w") as new_file:
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
                my_file.write(f"{name:30}{dict2[id]:<10}{points:<10}{dict3[id]:<10}{abc:<10}{g}\n")
                new_file.write(f"{id};{name};{g}\n")
print("Results written to files results.txt and results.csv")