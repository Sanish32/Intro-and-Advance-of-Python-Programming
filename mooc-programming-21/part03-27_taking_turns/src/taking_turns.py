# Write your solution here
number=int(input("Please type in a number:"))
i=0
if number % 2 ==0:
    while i < number:
        print(i+1)
        print(number)
        i+=1
        number-=1
elif number % 2 != 0:
    while i < number:
        print(i+1)
        if i+1 == number:
            break
        print(number)
        i+=1
        number-=1