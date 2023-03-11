# write your solution here
import difflib
def check(abc:list):
    sen=""
    new=[]
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
            new.append(abc[i])
            sen+="*"+abc[i]+"* "
    print(sen)
    print("suggestions:")
    words=[]
    with open("wordlist.txt") as new_file:
            for line in new_file:
                line=line.strip()
                words.append(line)
    for x in new:
        print(f"{x}:"+",".join(difflib.get_close_matches(x,words)))
    
sentence=input("Write text:")
abc=sentence.split()
check(abc)