# Write your solution here
wage=float(input("Hourly wage:"))
worked=int(input("Hours worked:"))
day=input("Day of the week:")
if day != "Sunday":
    multi=wage*worked
if day == "Sunday":
    multi=wage*worked*2

print(f"Daily wages: {multi} euros")
