# Write your solution here
def filter_solutions():
    with open("solutions.csv") as new_file:
        for line in new_file:
            line=line.replace("\n","")
            parts=line.split(";")
          
            if "-" in parts[1]:
               new=parts[1].split("-")
            else:
               new=parts[1].split("+")
            a=0
            hello=parts[0]+";"+parts[1]+";"+parts[2]+"\n"
            print(hello)
            if (int(new[0])-int(new[1]))==int(parts[2]) or (int(new[0])+int(new[1]))==int(parts[2]):
                with open("correct.csv") as my_file:
                    for line in my_file:
                        if hello in line:
                            a=1
                    if a==0:
                        with open("correct.csv","a") as my_file:
                            my_file.write(hello)
                continue
            else:
                with open("incorrect.csv") as my_file:
                    for line in my_file:
                        if hello in line:
                            a=1
                    if a==0:
                        with open("incorrect.csv","a") as my_file:
                            my_file.write(hello)
if __name__=="__main__":
   filter_solutions()
 
 