# write your solution here
def check(abc:list):
    sen=""
    for i in range(len(abc)):
        a=0
        with open("wordlist.txt") as new_file:
            for line in new_file:
                line=line.strip()
                if abc[i].lower()==line:
                    sen+=abc[i]+ " "
                    a=1
                    break
        if a==0:
            sen+="*"+abc[i]+"* "
    print(sen)
sentence=input("Write text:")
abc=sentence.split()
check(abc)