# Write your solution here
def even_numbers(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]%2==0:
            b.append(a[i])
        i+=1
    return b
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)