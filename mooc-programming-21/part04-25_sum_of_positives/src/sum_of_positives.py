# Write your solution here
def sum_of_positives(a):
    index=0
    sum=0
    while index<len(a):
        if a[index]>0:
            sum+=a[index]
        index+=1
    return sum
if __name__== "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
