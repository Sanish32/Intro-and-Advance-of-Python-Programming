# Write your solution here
def longest_series_of_neighbours(list):
    count=0
    great=0
    for i in range(len(list)):
        if i!=len(list)-1:
            if list[i]+1==list[i+1] or list[i]-1==list[i+1]:
                count+=1
                if count>great:
                    great=count
            elif list[i]+1!=list[i+1]:
                count=0
    return great+1
if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))