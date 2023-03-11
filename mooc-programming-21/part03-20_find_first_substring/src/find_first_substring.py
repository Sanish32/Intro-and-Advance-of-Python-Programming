# Write your solution here
word=input("Please type in a word:")
char=input("Please type in a character:")
a=word.find(char)
b=len(word)
i=0
c=True
if a != -1:
    while c:
        if a == (b-1):
            c=False
        elif a == (b-2):
            c=False
        else :
            print(word[a:a+3])
            c=False
