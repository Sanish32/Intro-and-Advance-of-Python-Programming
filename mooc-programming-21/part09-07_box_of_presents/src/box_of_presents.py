# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self,name:str,weight:int):
        self.name=name
        self.weight=weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.contents=[]


    def add_present(self,present:Present):
        self.contents.append(present)
    
    def total_weight(self):
        combined_weight=0
        for content in self.contents:
            combined_weight+=content.weight
        return combined_weight