# Write your solution here
import random 
import string 
def generate_strong_password(num,cond1=True,cond2=True):
    passwd=""
    y=0
    speci="!?=+-()#"
    word=[]
    word.append(random.choice([x for x in string.ascii_lowercase]))
    y+=1
    if num==2:
        x=random.randint(0,1)
        if x==0:
            word.append(str(random.randint(0,9)))
            y+=1
        elif x==1:
            word.append(random.choice(speci))
            y+=1
    elif num>3:
        if cond1 and cond2:
            word.append(str(random.randint(0,9)))
            word.append(random.choice(speci))
            y+=2
        elif cond1:
            word.append(str(random.randint(0,9)))
            y+=1
        elif cond2:
            word.append(random.choice(speci))
            y+=1
    for i in range(num-y):
        if not cond2 and not cond1:
            word.append(random.choice(string.ascii_lowercase))
        elif cond1 and not cond2:
            x=random.randint(0,1)
            if x==0:
                word.append(random.choice(string.ascii_lowercase))
            elif x==1:
                word.append(str(random.randint(0,9)))
        elif cond2 and not cond1:
            x=random.randint(0,1)
            if x==0:
                word.append(random.choice(string.ascii_lowercase))
            elif x==1:
                word.append(random.choice(speci))
        elif cond1 and cond2:
            x=random.randint(0,2)
            if x==0:
                word.append(random.choice(string.ascii_lowercase))
            elif x==1:
                word.append(random.choice(speci))
            elif x==2:
                word.append(str(random.randint(0,9)))
    random.shuffle(word)
    passwd="".join(word)
    return passwd
        
if __name__=="__main__":
    for i in range(10):
        print(generate_strong_password(5, True, True))