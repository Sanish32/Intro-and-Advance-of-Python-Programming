# Write your solution here
num1=int(input("Number 1:"))
num2=int(input("Number 2:"))
oper=input("Operation:")
if oper == "add":
    sum=num1+num2
    print(f"{num1} + {num2} = {sum}") 
if oper == "multiply":
    multi=num1*num2
    print(f"{num1} * {num2} = {multi}") 
if oper == "subtract":
    diff=num1-num2
    print(f"{num1} - {num2} = {diff}") 
