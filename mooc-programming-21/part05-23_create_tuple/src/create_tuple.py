# Write your solution here
def create_tuple(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        big=num1
    elif num2>=num3:
        big=num2
    else:
        big=num3
    if num1<=num2 and num1<=num3:
        small=num1
    elif num2<=num3:
        small=num2
    else:
        small=num3
    sum=num1+num2+num3
    tuple=(small,big,sum)
    return tuple
if __name__ == "__main__":
    r=print(create_tuple(5, 3, -1))
    print(r)