# Write your solution here
def squared(string,num):
    i=0
    row=string*num*num
    while i < num:
        print(row[0:num])
        row=row[num:]
        i+=1
if __name__ == "__main__":
    squared("ab",3)
    squared("aybabtu",5)
            