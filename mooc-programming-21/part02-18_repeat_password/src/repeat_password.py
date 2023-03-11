# Write your solution here
password=input("Password:")
while True:
    repeat=input("Repeat password:")
    if password != repeat:
        print("They do not match!")
    else:
        break
print("User account created!")