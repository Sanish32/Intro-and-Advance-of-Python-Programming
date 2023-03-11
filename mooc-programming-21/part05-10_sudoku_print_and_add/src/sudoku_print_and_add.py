# Write your solution here
def print_sudoku(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j]==0:
                s[i][j]="_"
            else:
                continue
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j==len(s[i])-1:
                print(s[i][j])
            elif j==2 or j==5:
                print(s[i][j], end="  ")
            else:
                print(s[i][j], end=" ")
        if i==2 or i==5:
            print()
def add_number(s,num1,num2,num3):
    s[num1][num2]=num3
if __name__=="__main__":
    s = [
  [ 9, "_", "_", "_", 8, "_", 3, "_", "_" ],
  [ 2, "_", "_", 2, 5, "_", 7, "_", "_" ],
  [ "_", 2, "_", 3, "_", "_", "_", "_", 4 ],
  [ 2, 9, 4, "_", "_", "_", "_", "_", "_" ],
  [ "_", "_", "_", 7, 3, "_", 5, 6, "_" ],
  [ 7, "_", 5, "_", 6, "_", 4, "_", "_" ],
  [ "_", "_", 7, 8, "_", 3, 9, "_", "_" ],
  [ "_", "_", 1, "_", "_", "_", "_", "_", 3 ],
  [ 3, "_", "_", "_", "_", "_", "_", "_", 2 ],
    ]
    print_sudoku(s)
    add_number(s, 0, 0, 2)
    add_number(s, 1, 2, 7)
    add_number(s, 5, 7, 3)
    print("Three numbers added:")
    print_sudoku(s)