# Write your solution here
def range_of_list(a):
    i=1
    big=a[0]
    small=a[0]
    while i<len(a):
        if small>a[i]:
            small=a[i]
        if big<a[i]:
            big=a[i]
        i+=1
    difference=big-small
    return difference
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)