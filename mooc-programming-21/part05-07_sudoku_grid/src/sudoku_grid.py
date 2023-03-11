def sudoku_grid_correct(list):
    for i in range(0,3):
        count=0
        for j in range(0,3):
            if j==0:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(0,3):
        count=0
        for j in range(3,6):
            if j==3:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(0,3):
        count=0
        for j in range(6,9):
            if j==6:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(3,6):
        count=0
        for j in range(0,3):
            if j==0:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(3,6):
        count=0
        for j in range(3,6):
            if j==3:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(3,6):
        count=0
        for j in range(6,9):
            if j==6:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(6,9):
        count=0
        for j in range(0,3):
            if j==0:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(6,9):
        count=0
        for j in range(3,6):
            if j==3:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    for i in range(6,9):
        count=0
        for j in range(6,9):
            if j==6:
                check=list[i][j]
            if check==list[i][j] and list[i][j]!=0:
                count+=1
                if count==2:
                    return False
    return True
if __name__=="__main__":
  sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
  print(sudoku_grid_correct(sudoku))
