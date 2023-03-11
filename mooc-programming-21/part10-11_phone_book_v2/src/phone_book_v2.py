# Tee ratkaisusi tähän:
class PhoneBook:
    def __init__(self):
        self.__persons = {}
        
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
        

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        elif name in self.__persons and len(self.__persons[name].numbers())==0:
            return None
        return self.__persons[name].numbers()

    def add_address(self,name,address):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_address(self,name):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()
    
    def get_entry(self,name):
        if not name in self.__persons:
            return None
        return 

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        addresses=self.__phonebook.get_address(name)
        print(numbers)
        print(addresses)
        if numbers == None and addresses==None:
            print("number unknown") 
            print("address unknown") 
            return 
        if numbers == None:
            print("number unknown") 
        else:
            for number in numbers:
                print(number)     

        if addresses == None:
            print("address unknown") 
        else:
            print(addresses)      

    def add_address(self):
        name = input("name: ")
        address=input("address: ")
        self.__phonebook.add_address(name,address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command=="3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self,name:str):
        self.names=name
        self.num=[]
        self.add=""

    def name(self):
        return self.names

    def numbers(self):
        return self.num

    def address(self):
        if self.add=="":
            return None
        return self.add

    def add_address(self,address):
        self.add=address

    def add_number(self,number):
        self.num.append(number)

# when testing, no code should be outside application except the following:
abc=PhoneBookApplication()
abc.execute()

    


