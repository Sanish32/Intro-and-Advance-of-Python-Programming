# Write your solution here
year=int(input("Year:"))
leap=0
while True:
    leap=year
    if year % 4 ==0:
        leap+=4
    elif year % 4 ==1:
        leap+=3
    elif year % 4== 3:
        leap+=1
    elif year % 4==2:
        leap+=2
    if leap % 100==0:
        if leap % 400==0:
            break
        elif leap % 400!=0:
            leap+=4
    break
print(f"The next leap year after {year} is {leap}")