# Write your solution here
def chessboard(num):
    a=0
    i=0
    a=int(num/2)
    b=num-1
    if num%2==0:
        while i< num:
            if i%2==0:
                print("10"*a)  
            elif i%2==1:
                print("01"*a)
            i+=1
    elif num%2==1:
        while i< num:
            j=0
            while j<num:
                if i%2==0:
                    if j!= b:
                        if j%2==0:
                            print("1",end="")
                        elif j%2==1:
                            print("0",end="")
                    elif j==b:
                        if j%2==0:
                            print("1")
                            break
                        elif j%2==1:
                            print("0")
                            break
                elif i%2==1:
                    if j!= b:
                        if j%2==0:
                            print("0",end="")
                        elif j%2==1:
                            print("1",end="")
                    elif j==b:
                        if j%2==0:
                            print("0")
                        elif j%2==1:
                            print("1")
                j+=1
            i+=1
# Testing the function
if __name__ == "__main__":
    chessboard(3)
