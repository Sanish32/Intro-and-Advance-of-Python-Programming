# Write your solution here
c1=0
c2=0
c3=0
c4=0
c5=0
c0=0
sum=0
times=0
while True:
    points=input("Exam points and exercises completed:")
    if points=="":
        break
    new=points.split()
    exam_points=int(new[0])
    exercises=int(new[1])
    grade=0
    for i in range(100,10,-10):
        if exercises<=i and exercises>=i-1-10:
            exercises_points=(int(exercises)//10)
            break
    total=exam_points+exercises_points
    sum+=total
    times+=1
    if exam_points<10:
        c0+=1
        continue
    if total>27 and total<31:
        grade=5
        c5+=1
    elif total>23:
        grade=4
        c4+=1
    elif total>20:
        grade=3
        c3+=1
    elif total>17:
        grade=2
        c2+=1
    elif total>14:
        grade=1
        c1+=1
    else:
        grade=0
        c0+=1
average=float((sum)/times)
pp=((c1+c2+c3+c4+c5)/times)*100
print("Statistics:")
print(f"Points average: {average}")
print(f"Pass percentage: {pp:.1f}")
print("Grade distribution:")
print(" 5:","*"*c5)
print(" 4:","*"*c4)
print(" 3:","*"*c3)
print(" 2:","*"*c2)
print(" 1:","*"*c1)
print(" 0:","*"*c0)
