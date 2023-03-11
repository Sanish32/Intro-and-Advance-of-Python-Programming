# Write your solution here
def remove_smallest(numbers):
    small=min(numbers)
    numbers.remove(small)
if __name__ == "__main__":
    numbers = [1,2]
    remove_smallest(numbers)
    print(numbers)