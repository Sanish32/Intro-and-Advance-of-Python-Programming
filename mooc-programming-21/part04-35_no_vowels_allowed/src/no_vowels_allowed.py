# Write your solution here
def no_vowels(str):
    vowel="aeiou"
    for n in str:
        if n in vowel:
            str=str.replace(n,"")
    return str
if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))