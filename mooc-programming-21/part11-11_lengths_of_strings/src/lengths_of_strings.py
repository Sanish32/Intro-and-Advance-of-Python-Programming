# WRITE YOUR SOLUTION HERE:
def lengths(items):
        return {item :len(item) for item in items}
if __name__=="__main__":
    
    word_list=["once","upto","a","time","in"]
    word_lengths=lengths(word_list)
    print(word_lengths)