# Write your solution here
def all_the_longest(a):
    longest=[]
    i=0
    long=0
    for item in a:
        if len(item)>=long:
            long=len(item)
    for i in range(0,len(a),1):
        if len(a[i])==long:
            longest.append(a[i])
    return longest
if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)   
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]    
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']