# Write your solution here
string=input("Please type in a string:")
substring=input("Please type in a substring:")
c=True
a=len(string)
count=0
i=0
e=len(string)
d=0
i=0
if substring in string:
    while i<e:
        b=string.find(substring)
        if b+3>a:  
            break   
        elif substring in string:
            if i==0:
                d+=b+2
            elif i==1:
                d+=b+1
            string=string[b+3:]
            count+=1
        else:
            break
        if count==2:
            print(f"The second occurrence of the substring is at index {d}.")
            break
        i+=1
if count==1 or count ==0:
    print("The substring does not occur twice in the string.")

