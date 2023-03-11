# Write your solution here
def anagrams(word1,word2):
    str1=sorted(word1)
    str2=sorted(word2)
    if str1==str2:
        return True
    elif str1!=str2:
        return False
if __name__ == "__main__":
    str1=input("String1:")
    str2=input("String2:")
    print(anagrams("tame", "meta")) 
    print(anagrams("tame", "mate")) 
    print(anagrams("tame", "team"))
    print(anagrams("tabby", "batty")) 
    print(anagrams("python", "java")) 