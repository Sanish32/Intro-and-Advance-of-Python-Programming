# Write your solution here
def oldest_person(people):
    elder=""
    say=10000
    for person in people:
        if say>=person[1]:
            elder=person[0]
            say=person[1]
    return elder
if __name__=="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people))
