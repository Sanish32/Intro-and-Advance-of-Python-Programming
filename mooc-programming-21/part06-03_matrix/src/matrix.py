def row_sums():
    with open("matrix.txt") as new_file:
        total=[]
        for line in new_file:
            sum=0
            line=line.replace("\n","")
            content=line.split(",")
            for items in content:
                sum+=int(items)
            total.append(sum)
    return total
def matrix_max():
    with open("matrix.txt") as new_file:
        max=0
        for line in new_file:
            line=line.replace("\n","")
            content=line.split(",")
            for items in content:
                if max<int(items):
                    max=int(items)
    return max
def matrix_sum():
    with open("matrix.txt") as new_file:
        sum=0
        for line in new_file:
            line=line.replace("\n","")
            content=line.split(",")
            for items in content:
                sum+=int(items)
    return sum
if __name__=="__main__":
    row_sums()
    matrix_sum()
    matrix_max()