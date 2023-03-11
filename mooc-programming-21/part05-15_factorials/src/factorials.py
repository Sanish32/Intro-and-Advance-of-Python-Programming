# Write your solution here
def factorials(n):
    dictionary={}
    i=1
    while i<n+1:
        j=1
        dictionary[i]=1
        while j<=i:
            dictionary[i]*=j
            j+=1
        i+=1
    return dictionary
if __name__=="__main__":
    k=factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])