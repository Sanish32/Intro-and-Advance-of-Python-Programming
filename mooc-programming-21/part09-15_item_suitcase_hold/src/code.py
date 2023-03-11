# Write your solution here:
class Item:
    def __init__(self,name,weight):
        self.__name=name
        self.__weight=weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self,max_weight):
        self.max_weight=max_weight
        self.total=0
        self.thing=[]

    def add_item(self,item:Item):
        if  self.max_weight>=(item.weight()+self.total):
            self.total+=item.weight()
            self.thing.append(item)

    def __str__(self):
        if len(self.thing)==1:
            return f"{len(self.thing)} item ({self.total} kg)"
        return f"{len(self.thing)} items ({self.total} kg)"


    def print_items(self):
        for item in self.thing:
            print(item)

    def weight(self):
        return self.total

    def heaviest_item(self):
        if len(self.thing)==0:
            return None
        heavy=0
        for items in self.thing:
            if heavy<items.weight():
                heavy=items.weight()
        for item in self.thing:
            if heavy==item.weight():
                return item

class CargoHold:
    def __init__(self,max):
        self.max=max
        self.cargo=[]
        self.all=0
    
    def add_suitcase(self,item:Item):
        if  self.max>=(item.weight()+self.all):
            self.all+=item.weight()
            self.cargo.append(item)

    def print_items(self):
        for items in self.cargo:
            items.print_items()

    def __str__(self):
        if len(self.cargo)==1:
            return f"{len(self.cargo)} suitcase, space for {self.max-self.all} kg"
        return f"{len(self.cargo)} suitcases, space for {self.max-self.all} kg"


if __name__=="__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()