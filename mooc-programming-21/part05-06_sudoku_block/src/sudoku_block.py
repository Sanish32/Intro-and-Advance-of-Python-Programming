def block_correct(list,r,c):
    new=[]
    for i in range(r,r+3):
        for j in range(c,c+3):
            new.append(list[i][j])
    for item in new:
        count=0
        for i in range(1,10):
            check=item
            if check==new[i-1] and new[i-1]!=0:
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
  print(block_correct(sudoku, 0, 3))
