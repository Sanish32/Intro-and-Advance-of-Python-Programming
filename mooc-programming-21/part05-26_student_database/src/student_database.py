# Write your solution here
def add_student(s,name):
    s[name]={}
    return s

def print_student(s,name):
    x=0
    for key,value in s.items():
        if key==name:
            if len(s[name])==0:
                print(f"{name}: \n no completed courses")
            else:
                print(f"{len(s[name])} completed courses:")
                print(f"{s[name][0]}")
            x+=1
    if x==0:
        print(f"{name}: no such person in the database")

def add_course(s,name,tuple):
    for key,value in s.items():
        if key==name:
            s[name][tuple[0]]=tuple[1]

if __name__=="__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print(students,"Peter")