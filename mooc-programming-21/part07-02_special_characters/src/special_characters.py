# Write your solution here
from string import ascii_letters, punctuation
def separate_characters(parts: str):
    ascii=""
    punc=""
    other=""
    tuple=()
    for item in parts:
        if item in ascii_letters:
            ascii+=item
        elif item in punctuation:
            punc+=item
        else: 
            other+=item
    tuple=(ascii,punc,other)
    return tuple
if __name__=="__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
