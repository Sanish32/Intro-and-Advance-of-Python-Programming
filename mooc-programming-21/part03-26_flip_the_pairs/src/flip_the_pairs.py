# Write your solution here
number=int(input("Please type in a number:"))
i=1
while i <= number:
    first=i
    second=i+1
    if number % 2 == 1 and i == number:
        print(first)
        break
    print(second)
    print(first)
    i+=2
    