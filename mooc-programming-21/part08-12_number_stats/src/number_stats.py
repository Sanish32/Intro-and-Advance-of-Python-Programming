# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers =0
        self.count=0
        self.even=0
        self.odd=0


    def get_sum_even(self):
        return self.even

    def get_sum_odd(self):
        return self.odd

    def add_number(self, number:int):
        self.numbers+=number
        self.count+=1

        if number%2==0:
            self.even+=number

        elif number%2==1:
            self.odd+=number
        

    def count_numbers(self):
        return self.count

    def get_sum(self):  
        return self.numbers

    def average(self):
        if self.count==0:
            return 0
        return (self.numbers)/(self.count)

    
stats=NumberStats()
while True:
    num=int(input("Please type in integer numbers:"))
    if num==-1:
        break
    else:
        stats.add_number(num)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.get_sum_even()}")
print(f"Sum of odd numbers: {stats.get_sum_odd()}")
