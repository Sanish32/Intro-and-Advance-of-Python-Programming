# Write your solution here:
class Person:
    def __init__(self,name:str):
        self.name=name
    def return_first_name(self):
        idk=self.name.split()
        return idk[0]
    def return_last_name(self):
        idk=self.name.split()
        return idk[1]


if __name__=="__main__":
    idk=[]

    peter=Person("Peter Python")
    print(peter.return_first_name())
    print(peter.return_last_name())


    paula=Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())