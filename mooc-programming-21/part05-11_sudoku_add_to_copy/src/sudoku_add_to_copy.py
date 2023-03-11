# Write your solution here
def print_sudoku(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j==len(s[i])-1:
                print(s[i][j])
            elif j==2 or j==5:
                print(s[i][j], end="  ")
            else: 
                print(s[i][j],end=" ")
def copy_and_add(s,r,c,num):
    new=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(s)):
        for j in range(len(s[i])):
            new[i].append(s[i][j])
    new[r][c]=num
    return new
if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print("Copy:")
    print_sudoku(grid_copy)