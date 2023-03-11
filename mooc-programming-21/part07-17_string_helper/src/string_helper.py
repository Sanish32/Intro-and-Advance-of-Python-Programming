# Write your solution here
import string
def change_case(what:str):
    new=list(what)
    for i in range(len(new)):
        if new[i] in string.ascii_lowercase:
            new[i]=new[i].upper()
        elif new[i].isupper():
            new[i]=new[i].lower()
    word="".join(new)
    return word

def split_in_half(what):
    x=len(what)
    if x%2==0:
        word1=what[:int(x/2)]
        word2=what[int(x/2):]
    elif x%2==1:
        word1=what[:int(x/2)]
        word2=what[int(x/2):]

    return word1,word2

def remove_special_characters(what):
    new=list(what)
    for x in list(what):
        if x not in string.ascii_letters and x!=" " and not x.isdigit():
            new.remove(str(x))

    word="".join(new)
    return word

if __name__=="__main__":
    import string_helper

    my_string = "Well hello there!"

    print(string_helper.change_case(my_string))

    p1, p2 = string_helper.split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)   