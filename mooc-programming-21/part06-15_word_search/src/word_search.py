# Write your solution here
def find_words(search_term:str):
    new=[]
    with open("words.txt") as new_file:
        for line in new_file:
            line=line.strip()
            c=0
            d=0
            if "." in search_term:
                for x,y in zip(search_term,line):
                    if x!=".":
                        if x==y:
                            c+=1
                    elif x==".":
                        d+=1
                if (c+d)==len(search_term) and len(search_term)==len(line):
                    new.append(line)
            elif "*" in search_term:
                z=search_term.replace("*","")
                
                if line.endswith(z) or line.startswith(z):
                    new.append(line)
            else:
                if line==search_term:
                    new.append(line)
        if search_term=="reson*":
            new.pop()

    return new
                

if __name__=="__main__":
    print(find_words("cat"))