# Write your solution here
word=input("Please type in a word:")
char=input("Please type in a character:")
i=0
b=len(word)
while i<b:
    a=word.find(char)
    if a+3 > len(word) or a==-1:
        break
    print(word[a:a+3])
    word=word[a+1:]
    i+=1
