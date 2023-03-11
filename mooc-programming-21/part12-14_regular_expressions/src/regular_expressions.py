# Write your solution here
import re
def is_dotw(my_string:str):
    abc=re.compile("Mon|Tue|Wed|Thu|Fri|Sat|Sun")
    if abc.search(my_string):
        return True
    return False    


def all_vowels(my_string:str):
    abc=re.compile("a|e|i|o|u|y")
    x=len(my_string)
    count=0
    for item in my_string:
        if abc.search(item):
            count+=1

    if count==x:
        return True
    return False

def time_of_day(my_string:str):
    words=my_string.split(":")
    y=re.compile("[0-5][0-9]")
    
    for word in words:
        for item in word:
            if item in "abcdefghijklmnopqrstuvwxyz":
                return False
    if (int(words[0]) >=0 and int(words[0])<=24) and y.search(words[1]) and y.search(words[2]):
        return True
    return False 


if __name__=="__main__":
    print(time_of_day("12:12:12"))