# Write your solution here
def shortest(list):
    short=list[0]
    for item in list:
        if len(item)<len(short):
            short=item
    return short
if __name__=="__main__":    
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
