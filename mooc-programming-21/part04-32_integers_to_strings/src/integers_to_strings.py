# Write your solution here
def formatted(a):
    list=[]
    b=""
    for item in a:
        b=f"{item:.2f}"
        list.append(b)
    return list
if __name__=="__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)