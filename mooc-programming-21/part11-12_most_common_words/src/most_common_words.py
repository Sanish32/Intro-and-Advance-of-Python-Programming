# WRITE YOUR SOLUTION HERE:
def most_common_words(x,lower_limit:int):
    xyz={}
    words=[]
    with open(x) as new_file:
        for lines in new_file:
            lines=lines.split()
            for line in lines:
                if "." in line:
                    line=line.strip(".")
                if "," in line:
                    line=line.strip(",")
                words.append(line)
    print(words)
    for word in words:
        xyz[word]=words.count(word)
    return {word:xyz[word] for word in xyz if xyz[word]>=lower_limit}

if __name__=="__main__":
    print(most_common_words("programming.txt",3))