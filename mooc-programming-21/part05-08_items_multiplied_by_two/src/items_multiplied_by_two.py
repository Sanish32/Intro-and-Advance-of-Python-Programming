# Write your solution here
def double_items(list):
    i=0
    new=[]
    while i<len(list):
        new.append(list[i]*2)
        i+=1
    return new
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)