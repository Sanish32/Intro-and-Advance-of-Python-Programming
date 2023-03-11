# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self,another:"RealProperty"):
        return self.square_metres>another.square_metres

    def price_difference(self,another:"RealProperty"):
        x=self.square_metres*self.price_per_sqm-another.square_metres*another.price_per_sqm
        if x>0:
            return x
        return x*(-1)
    
    def more_expensive(self,another:"RealProperty"):
        return  self.square_metres*self.price_per_sqm>another.square_metres*another.price_per_sqm
