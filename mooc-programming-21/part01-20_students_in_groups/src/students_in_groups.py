# Write your solution here
student=int(input("How many students on the course?"))
group_size=int(input("Desired group size?"))
group_formed=student//group_size
if student % 2 == 0:
    if student == 200:
        print(f"Number of groups formed: {group_formed+1}")
    if student != 200:
        print(f"Number of groups formed: {group_formed}")
elif student % 2 == 1:
    print(f"Number of groups formed: {group_formed+1}")

