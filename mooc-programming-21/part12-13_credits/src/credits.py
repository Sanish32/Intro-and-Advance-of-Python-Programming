from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

    def get_credit(self):
        return self.credits

def sum(abc,item):
    return abc+item.get_credit()

def sum_of_all_credits(items):
    x=reduce(sum,items,0)
    return x

def sum_of_passed_credits(items):
    xyz=list(filter(lambda x:x.grade!=0,items))
    abc=reduce(lambda reduced_sum,item:reduced_sum+item.credits,xyz,0)
    return abc

def average(items):
    xyz=list(filter(lambda x:x.grade!=0,items))
    x=len(xyz)
    abc=reduce(lambda reduced_sum,item:reduced_sum+item.grade,xyz,0)
    mean=abc/x
    return mean

# Write your solution
if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)