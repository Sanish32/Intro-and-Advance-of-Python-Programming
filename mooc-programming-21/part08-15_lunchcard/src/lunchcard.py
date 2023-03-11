# Write your solution here:
class LunchCard:
    def __init__(self,balance:float):
        self.balance=balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        try:
            if 2.60<self.balance:
                self.balance-=2.60
        except:
            pass
    
    def eat_special(self):
        try:
            if 4.60<self.balance:
                self.balance-=4.60
        except:
            pass
    
    def deposit_money(self,cash):
        if cash<0:
            raise ValueError
        self.balance+=cash

Peter= LunchCard(20)
Grace=LunchCard(30)
Peter.eat_special()
Grace.eat_lunch()
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")
Peter.deposit_money(20)
Grace.eat_special()
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")
Peter.eat_lunch()
Peter.eat_lunch()
Grace.deposit_money(50)
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")

  