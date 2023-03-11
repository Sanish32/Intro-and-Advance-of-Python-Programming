# Write your solution here
def who_won(list):
    count1=0
    count2=0
    for item in list:
        for num in item:
            if num==1:
                count1+=1
            elif num==2:
                count2+=1
            else:
                continue
    if count1 > count2:
        return 1
    elif count2 > count1:
        return 2
    else:
        return 0
if __name__=="__main__":
    my_list=[[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(my_list))