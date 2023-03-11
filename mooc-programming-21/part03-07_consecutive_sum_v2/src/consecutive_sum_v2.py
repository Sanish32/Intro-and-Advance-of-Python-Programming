# Write your solution here
limit=int(input("Limit:"))
num=1
sum=0
word=""
while sum<limit:
    sum+=num
    word+=str(num)
    if sum < limit:
        word+=" + "
    if sum == limit or sum > limit:
        continue
    num+=1
print(f"The consecutive sum: {word} = {sum}")