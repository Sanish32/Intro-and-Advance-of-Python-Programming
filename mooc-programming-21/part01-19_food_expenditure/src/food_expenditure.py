# Write your solution here
atcafe=float(input("How many times a week do you eat at the student cafeteria?"))
student_lunch=float(input("The price of a student lunch?"))
groceries=float(input("How much money do you spend on groceries in a week?"))
weekly=groceries+student_lunch*atcafe
daily=weekly/7
print("\nAverage food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")