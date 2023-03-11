# Write your solution here
def everything_reversed(list):
    new=list[::-1]
    print(new)
    i=0
    while i<len(new):
        new.insert(i,new[i][::-1])
        new.pop(i+1)
        i+=1
    return new
if __name__=="__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)