# Write your solution here
def row_sums(matrix):
    sum=0
    for items in matrix:
        for item in items:
            sum+=item
        items.append(sum)
        sum=0
if __name__=="__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)