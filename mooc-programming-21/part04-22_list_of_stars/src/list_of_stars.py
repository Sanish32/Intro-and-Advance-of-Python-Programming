# Write your solution here
def list_of_stars(a):
    i=0
    while i<len(a):
        print("*"*a[i])
        i+=1
if __name__ == "__main__":
    list=[3,7,1,1,2]
    list_of_stars(list)