# Write your solution here
from datetime import date, datetime
d=int(input("Day:"))
m=int(input("Month:"))
y=int(input("Year:"))
dob=datetime(y,m,d)
millennium=datetime(1999,12,31)
if dob<=millennium:
    age=millennium-dob
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")