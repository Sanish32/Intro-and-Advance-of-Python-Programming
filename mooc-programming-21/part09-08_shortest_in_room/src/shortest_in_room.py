# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name



class Room:
    def __init__(self):
        self.people=[]
        

    def add(self,person:Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people)==0
    

    def print_contents(self):
        combined_height=0
        for person in self.people:
            combined_height+=person.height
        print(f"There are {len(self.people)} persons in the room, and their combined height is {combined_height} cm") 

        for person in self.people:
            print(f"{person} ({person.height} cm)")

    def shortest(self):
        if len(self.people)!=0:
            shortest_height=self.people[0].height
            short_name=self.people[0].name
            for person in self.people:
                if shortest_height>person.height:
                    shortest_height=person.height
                    short_name=person.name
        
            for person in self.people:
                if person.name==short_name:
                    return person
        return None
                
    def remove_shortest(self):
        shortest_person=self.shortest()
        if shortest_person !=None:
            self.people.remove(shortest_person)
        return shortest_person
 


if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()