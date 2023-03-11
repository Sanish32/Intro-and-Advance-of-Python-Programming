# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []
 
    def number_of_items(self):
        return len(self.products)
 
    def add(self, goods: str, amount: int):
        self.products.append((goods, amount))
 
    def item(self, n: int):
        return self.products[n - 1][0]
 
    def amount(self, n: int):
        return self.products[n - 1][1]
def total_units(list):
    sum=0
    for i in range(1,list.number_of_items()+1):
        sum+=list.amount(i)
    return sum
# -------------------------
# Write your solution here:
# -------------------------
if __name__=="__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)
    print(my_list.number_of_items())
    print(my_list.item(1))
    print(my_list.amount(1))
    print(my_list.item(2))
    print(my_list.amount(2))
    print(total_units(my_list))