# Write your solution here
fahren=int(input("Please type in a temperature(F):"))
celsius=(fahren-32)*(5/9)
if celsius < 0:
    print(f"{fahren} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
if celsius >= 0:
    print(f"{fahren} degrees Fahrenheit equals {celsius} degrees Celsius")
