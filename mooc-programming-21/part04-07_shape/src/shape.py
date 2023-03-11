# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def shape(num1,str1,num2,str2):
    for i in range(1,num1+1,1):
        line(i,str1)
    for j in range(1,num2+1,1):
        line(num1,str2)
def line(number,string):
    if string=="":
        char="*"
    else:
        char=string[0]
    print(char*number)
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    shape(2,"o",4,"+")
    shape(3,".",0,",")