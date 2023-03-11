# Write your solution here
def spruce(num):
    print("a spruce!")
    i=0
    for i in range(0,num+1,1):
        if i==(num):
            print(" "*(num-1)+"*")
        else:
            print(" "*(num-i-1)+"*"+"**"*i)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)