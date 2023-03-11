# Write your solution here
def row_correct(name,num):
    i=0
    check=0
    while i<len(name[num]):
        check=name[num][i]
        for j in range(0,9,1):
            if check==0:
                break
            if i!=j and check==name[num][j]:
                return False
        i+=1
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
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))