# Write your solution here
def longest(word):
    long=""
    for item in word:
        if len(item)>len(long):
            long=item
    return long
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))