# Write your solution here
first=input("1st letter:")
second=input("2nd letter:")
third=input("3rd letter:")
if (first > second and second > third) or (third > second and second > first):
    print(f"The letter in the middle is {second}")
elif (second > first and first > third) or (third > first and first > second):
    print(f"The letter in the middle is {first}")
elif (second > third and third > first) or (first > third and third > second):
    print(f"The letter in the middle is {third}")

