def read_fruits():
    with open("fruits.csv") as new_file:
        dict={}
        for line in new_file:
            line=line.replace("\n","")
            words=line.split(";")
            dict[words[0]]=float(words[1])
    return dict

# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        new={}
        for line in new_file:
            line=line.replace("\n"," ") 
            value=line.split(";")
            new[value[0]]=float(value[1])
    return new
if __name__=="__main__":
    print(read_fruits())

