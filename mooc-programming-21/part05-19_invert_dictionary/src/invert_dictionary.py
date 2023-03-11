# Write your solution here
def invert(dict):
    new={}
    for item in dict:
        new[dict[item]]=item
    dict.clear()
    for item in new:
        dict[item]=new[item]
    print(dict)
if __name__=="__main__":
    dict = {1: 10, 2: 20, 3: 30}
    invert(dict)
    