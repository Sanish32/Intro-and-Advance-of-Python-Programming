def palindromes(str):
    word=[]
    check=[]
    for item in str:
        word.append(item)
        check.append(item)
    check.reverse()
    length=len(word)
    i=0
    count=0
    while i<length:
        if word[i]==check[i]:
            count+=1
        i+=1
    if count==length:
        return True
    return False
while True:
    string=input("Please type in a palindrome:")
    result=palindromes(string)
    if result==True:
        print(f"{string} is a palindrome!")
        break
    print("that wasn't a palindrome")