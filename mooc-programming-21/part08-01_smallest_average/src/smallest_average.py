# Write your solution here
def average(dict):
    sum=0
    for key in dict:
        if key!="name":
            sum+=dict[key]
    average=float(sum/3)
    return average
def smallest_average(p1,p2,p3):
    if average(p1)<average(p2) and average(p1)<average(p3):
        return p1
    elif average(p2)<average(p3):
        return p2
    return p3
if __name__=="__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))

