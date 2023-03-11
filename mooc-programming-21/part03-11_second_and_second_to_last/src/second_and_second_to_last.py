# Write your solution here
string=input("Please type in a string:")
second=string[1]
last_second=string[-2]
if second== last_second:
    print("The second and the second to last characters are "+second)
else:
    print("The second and the second to last characters are different")