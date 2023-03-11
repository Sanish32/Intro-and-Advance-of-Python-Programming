# Write your solution here
def search_by_name(filename:str,word:str):
    new=[]
    dict={}
    a=""
    with open(filename) as new_file:
        for line in new_file:
            line=line.replace("\n","")
            now_line=line
            if ""==line:
                continue
            elif line[0].isupper():
                a=now_line
                dict[a]=[]
            elif line[0].islower() or now_line.isnumeric():
                dict[a].append(line)
    
    for x in dict:
        if word in x.lower():
            new.append(x)
    return new

def search_by_time(filename:str,prep_time:int):
    new=[]
    dict={}
    a=""
    with open(filename) as new_file:
        for line in new_file:
            line=line.replace("\n","")
            now_line=line
            if ""==line:
                continue
            elif line[0].isupper():
                a=now_line
                dict[a]=[]
            elif line[0].islower() or now_line.isnumeric():
                dict[a].append(line)
    for key,value in dict.items():
        if int(value[0])<=prep_time:
            new.append(key+f", preparation time {value[0]} min")

    return new

def search_by_ingredient(filename: str, ingredient: str):
    new=[]
    dict={}
    a=""
    with open(filename) as new_file:
        for line in new_file:
            line=line.replace("\n","")
            now_line=line
            if ""==line:
                continue
            elif line[0].isupper():
                a=now_line
                dict[a]=[]
            elif line[0].islower() or now_line.isnumeric():
                dict[a].append(line)

    for key,value in dict.items():
        for x in value:
            if x==ingredient:
                new.append(key+f", preparation time {value[0]} min")

    return new

if __name__=="__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)