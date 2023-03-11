# Write your solution here
while True:
    i=1
    factorial=1
    number=int(input("Please type in a number:"))
    if number == 0 or number < 0:
        break
    while i <= number:
        factorial*=i
        i+=1
    print(f"The factorial of the number {number} is {factorial}")
print("Thanks and bye!")