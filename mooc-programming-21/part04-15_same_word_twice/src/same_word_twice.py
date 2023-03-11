# Write your solution here
word=[]
i=0
count=0
c=True
while c:
    str=input("Words:")
    if str in word:
        c=False
    else:
        word.append(str)
        count+=1
print(f"You typed in {count} different words")
