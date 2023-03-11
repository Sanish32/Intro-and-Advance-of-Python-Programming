# Write your solution here
def list_sum(c,d):
    i=0
    e=[]
    while i<len(c):
        e.append(c[i]+d[i])
        i+=1
    return e
if __name__=="__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]