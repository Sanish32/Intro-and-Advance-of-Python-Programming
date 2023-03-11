# Write your solution here
def hash_square(num):
    i=0
    while i < num:
        j=0
        while j < num:
            if j == (num-1):
                print("#")
            elif j != (num-1):
                print("#",end="")
            j+=1
        i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)