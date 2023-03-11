# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as new_file:
        data=new_file.read()
    big=json.loads(data)
    for i in range(len(big)):
        print(big[i]["name"],end="",)
        print("",big[i]["age"],"years",end="",)
        if len(big[i]["hobbies"])==0:
            print(" ()\n")
        else:
            print(" (",end="")
        for j in range(len(big[i]["hobbies"])):
            if j+1!=len(big[i]["hobbies"]):
                print(big[i]["hobbies"][j], end=", ",)
            else:
                print(big[i]["hobbies"][j]+")")

if __name__=="__main__":
    file=input("Enter the file name:")
    print_persons(file)