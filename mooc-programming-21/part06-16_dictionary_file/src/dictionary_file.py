# Write your solution here
x=0
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    x=int(input("Function:"))
    if x==1:
        finnish=input("The word in Finnish:")
        english=input("The word in English:")
        words=finnish+"-"+english
        with open("dictionary.txt","a") as my_file:
           my_file.write(words+"\n")
        print("Dictionary entry added")
 
    elif x==2:
        s=input("Search term:")
        with open("dictionary.txt") as my_file:
            for line in my_file:
                line=line.strip()
                words=line.split("-")
                if s in words[0] or s in words[1]:
                   print(f"{words[0]} - {words[1]}")
                  
    elif x==3:
        print("Bye!")
        break
 


