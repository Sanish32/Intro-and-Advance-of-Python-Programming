# Write your solution here
def new_person(name: str, age: int):
    if name=="":
        raise ValueError("Name is empty string")
    elif " " not in name:
        raise ValueError("Name contains less than two words")
    elif len(name)>40:
        raise ValueError("Name is longer than 40 characters")
    if age<0:
        raise ValueError("Age is negative")
    elif age>150:
        raise ValueError("Age is greater than 150")
    tuple=(name,age)
    return tuple
if __name__=="__main__": 
    name=input("Name:")
    age=int(input("Age:"))       
    
    new_person(name,age)
