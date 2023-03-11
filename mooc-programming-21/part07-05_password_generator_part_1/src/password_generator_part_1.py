# Write your solution here
import string 
import random
def generate_password(num):
    abc=string.ascii_lowercase
    password=""
    for i in range(num):
        password=password+random.choice(abc)
    return password
if __name__=="__main__":
    length=int(input("Enter the desired length of the password:"))
    for i in range(10):
        print(generate_password(length))