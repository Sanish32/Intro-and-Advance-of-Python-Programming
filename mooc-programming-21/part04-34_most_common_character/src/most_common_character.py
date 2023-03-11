# Write your solution here
def most_common_character(str):
    great=0
    list=[]
    for item in str:
        list.append(item)
    for i in range(len(list)):
        word=list[i]
        c=0
        for j in range(len(list)):
            if word==list[j]:
                c+=1
                if great<c:
                    great=c
                    most=word
    return most
if __name__=="__main__":
    first_string = "aaabb"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))