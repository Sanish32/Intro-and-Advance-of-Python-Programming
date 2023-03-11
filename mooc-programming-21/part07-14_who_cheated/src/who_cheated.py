# Write your solution here
def cheaters():
    new=[]
    dict1={}
    dict2={}
    with open("start_times.csv") as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            dict1[words[0]]=words[1]


    with open("submissions.csv") as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            dict2[words[0]]=words[3]
            if int(words[1])>2:
                new.append(words[0])
    

    for key1,value1 in dict1.items():
        for key2,value2 in dict2.items():
            if key1==key2:
                a=value1.split(":")
                b=value2.split(":")
                x=int(b[0])-int(a[0])
                y=int(b[1])-int(a[1])
                if x>=3 and y>=0:
                    new.append(key1)
    new1=[]
    for i in new:
        if i not in new1:
            new1.append(i)
    print(new1)
    return new1
            
if __name__=="__main__":
    cheaters()