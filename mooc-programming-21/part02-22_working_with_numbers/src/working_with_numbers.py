# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count=0
sum=0
pos=0
neg=0
while True:
    number=int(input("Numbers:"))
    if number == 0:
        break
    sum+=number
    if number > 0:
        pos+=1
    elif number < 0:
        neg+=1
    count+=1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
mean=float(sum/count)
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")