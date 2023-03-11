# Write your solution here
def transpose(matrix):
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])):
            if i>j:
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    transpose(matrix)
    print(matrix)