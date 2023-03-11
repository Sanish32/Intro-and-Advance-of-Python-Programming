# WRITE YOUR SOLUTION HERE:
from collections import Counter
class ListHelper:
    def greatest_frequency(my_list:list):
        dict={}

        for items in my_list:
            dict[items]=my_list.count(items)
            x=dict[items]

        for items in dict:
            if x<dict[items]:
                x=dict[items]
 
        for items in dict:
            if x==dict[items]:
                return items
                
    def doubles(my_list:list):
        count=0
        dict={}

        for items in my_list:
            dict[items]=my_list.count(items)   
        
        for items in dict:
            if dict[items]>1:
                count+=1
        return count
 
if __name__=="__main__":
    numbers = [1, 2,3,1,1,2]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))