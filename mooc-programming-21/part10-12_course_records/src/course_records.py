# tee ratkaisusi tänne
class CourseRecord:
    total_courses=0
    total_credits=0
    def __init__(self):
        self.__persons = {}
        
        
    def add_course(self, course,grade,credits):
        if not course in self.__persons:
            self.__persons[course] = Student(course)
            CourseRecord.total_courses+=1
            CourseRecord.total_credits+=credits
        CourseRecord.total_credits
        x=self.__persons[course].add_course(grade,credits)
        

    def get_grade(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].grades()

    def get_credit(self,name):
        if not name in self.__persons:
            return None
        return self.__persons[name].credits()

    def calculate(self):
        x=len(self.__persons)
        y=0
        for key,value in self.__persons.items():
            x+=1
            y
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = CourseRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits=int(input("credits: "))
        self.__phonebook.add_course(course, grade,credits)
    
    def get_course_data(self):
        courses = input("course: ")
        grade = self.__phonebook.get_grade(courses)
        credit=self.__phonebook.get_credit(courses)
        if grade == None:
            print("no entry for this course") 
            return
        else:
            print(f"{courses} ({credit} cr) grade {grade}")        

    def statistics():
        print(f"{len(self.__phonebook.items()}")
        
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command=="3":
                self.statistics()
            else:
                self.help()

class Student:
    def __init__(self,course:str):
        self.course=course
        self.grade=0
        self.credit=0
        
    def courses(self):
        return self.course

    def grades(self):
        return self.grade

    def credits(self):
        return self.credit

    def add_course(self,grade,credit):
        self.credit=credit
        a=0
        if self.credit==0:
            self.grade=grade
        elif grade>self.grade:
            self.grade=grade
            a=1
        return a
            
        

# when testing, no code should be outside application except the following:
abc=PhoneBookApplication()
abc.execute()

    


