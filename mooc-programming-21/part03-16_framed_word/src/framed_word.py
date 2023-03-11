# Write your solution here
word=input("Word:")
print("*"*30)
a=len(word)
b=int(a/2)
if a%2==0:
    d=int((30-2-a)/2)
    c=str("*"+" "*d+word+" "*d+"*")
    print(c)
elif a%2!=0:
    d=int((30-2-a)/2)
    c=str("*"+" "*d+word+" "*d+" *")
    print(c)
print("*"*30)
