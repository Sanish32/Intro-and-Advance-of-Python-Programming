# Write your solution here
def filter_incorrect():
    with open("correct_numbers.csv","w") as my_file:
        with open("lottery_numbers.csv") as new_file:
            for line in new_file:
                a=0
                x=line
                line=line.replace("week ","")
                line=line.replace(";",",")
                line=line.strip()
                parts=line.split(",")
                
                if len(parts[1:])!=7:
                    a=1
                
                if not parts[0].isnumeric():
                    a=1

                for part in parts[1:]:
                    if not part.isnumeric() or int(part)<1 or int(part)>39:
                        a=1
                
                new=[]
                for part in parts[1:]:
                    if part not in new:
                        new.append(part)
                    else:
                        a=1

                if a==0:
                    my_file.write(x)
                
                new.clear()
  
      
if __name__=="__main__":
   filter_incorrect()
 
 
 
 
