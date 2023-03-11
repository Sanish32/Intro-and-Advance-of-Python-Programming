# Write your solution here
sentence=""
same=""
while True:
    word=input("Please type in a word:")
    if word == "end" or word == same:
        print(sentence)
        break
    sentence+=word+" "
    same = word