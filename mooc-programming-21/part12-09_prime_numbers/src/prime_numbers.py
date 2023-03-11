# Write your solution here
def prime_numbers():
    number=2
    items=[]
    while number>0:
        x=True
        if len(items)==0:
            yield number
            items.append(number)
            number+=1
        else:
            for item in items:
                if number%item==0:
                    x=False
            
            if x:
                yield number
                items.append(number)
            number+=1
            

if __name__=="__main__":
    numbers = prime_numbers()
    for i in range(3):
        print(next(numbers))