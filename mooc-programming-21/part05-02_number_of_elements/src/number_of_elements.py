# Write your solution here
def count_matching_elements(list,num):
    count=0
    for item in list:
        for value in item:
            if value==num:
                count+=1
    return count
if __name__=="__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
