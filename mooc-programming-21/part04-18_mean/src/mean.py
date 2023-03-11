# Write your solution here
def mean(b):
    i=0
    a=0
    for i in range(0,len(b),1):
        a+=b[i]
    mean=a/len(b)
    return mean
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)