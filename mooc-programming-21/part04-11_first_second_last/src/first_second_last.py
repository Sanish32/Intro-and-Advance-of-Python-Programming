# Write your solution here
def first_word(string1):
    new=string1.split()
    return new[0]
def second_word(string2):
    new=string2.split()
    if len(new)>1:
        return new[1]
def last_word(string3):
    new=string3.split()
    if len(new)>1:
        return new[-1]
    elif len(new)<=1:
        return new[2]
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))