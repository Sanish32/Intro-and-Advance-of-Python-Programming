# Write your solution here
def no_shouting(str):
    i=0
    new=[]
    while i<len(str):
        if str[i].isupper()==False:
            new.append(str[i])
        i+=1
    return new
if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)