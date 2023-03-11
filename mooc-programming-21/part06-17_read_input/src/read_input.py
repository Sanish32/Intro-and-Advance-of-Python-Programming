# Write your solution here
def read_input(str,num1,num2):
    while True:
        try:
            number=int(input(f"{str}"))
            if number>num1 and number<num2:
                return number
            else:
                print(f"You must type in an integer between {num1} and {num2}")
        except ValueError:
            print(f"You must type in an integer between {num1} and {num2}")


if __name__=="__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)