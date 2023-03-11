# Write your solution here
def same_chars(str,num1,num2):
    length=len(str)
    if length<=num1 or length<=num2 or str[num1]!=str[num2]:   
        return False
    elif str[num1]==str[num2]:
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 6, 7)) 
    print(same_chars("programmer", 0, 4)) 
    print(same_chars("programmer", 0, 12)) 