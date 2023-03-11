# Write your solution here
def times_ten(start,end):
    dictionary={}
    for i in range(start,end+1,1):
        dictionary[i]=i*10
    return dictionary
if __name__=="__main__":
    d = times_ten(3, 6)
    print(d)