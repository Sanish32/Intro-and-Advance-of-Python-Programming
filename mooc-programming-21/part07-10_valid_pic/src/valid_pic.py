# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    words=pic[:]
    a=""
    if len(words)!=11:
        return False
    if words[6]=="+":
        a="18"
    elif words[6]=="-":
        a="19"
    elif words[6]=="A":
        a="20"
    elif words[6]!="+" or words[6]!="-" or words[6]!="A":
        return False

    p="".join(words[7:10])
    d="".join(words[:2])
    m="".join(words[2:4])
    t="".join(words[4:6])
    y=a+t
    try:
        x=datetime(int(y),int(m),int(d))
    except:
        return False
        
    sum="".join(words[:6])+"".join(words[7:10])
    check=int(sum)%31
    print(check)
    given=[r for r in "0123456789ABCDEFHJKLMNPRSTUVWXY"]
    for i in range(len(given)):
        if check==i:
            b=given[i]
    print(b)
    if b==words[-1]:
        return True
    else:
        return False

    
if __name__=="__main__":
    str=input("Enter the PIC:")
    print(is_it_valid(str))
