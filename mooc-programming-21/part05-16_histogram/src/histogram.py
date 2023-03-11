# Write your solution here
def histogram(string):
    groups={}
    for word in string:
        if word not in groups:
            groups[word]=0
        groups[word]+=1
    for word in groups:
        print(f"{word} "+"*"*int(groups[word]))
if __name__=="__main__":
    print(histogram("abba"))
    
