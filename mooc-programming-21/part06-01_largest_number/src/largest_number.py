def largest():
   
    with open("numbers.txt") as new_file:
        new=[]
        for line in new_file:
            line=line.replace("\n","")
            new.append(int(line))

    new.sort()
    return new[-1]

if __name__=="__main__":
    largest()

# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest=0
        for line in new_file :
            num=int(line)
            if num>largest:
                largest=num
    return largest

if __name__=="__main__":
    result=largest()
    print(result)


