# Write your solution here:
from typing import NewType


class Series:
    def __init__(self,title:str,number_seasons:int,list_of_genre:list):
        self.title=title
        self.number_of_seasons=number_seasons
        self.list_of_genre=list_of_genre
        self.abc=[]

    def __str__(self):
        if len(self.abc)==0:
            return f"{self.title} ({self.number_of_seasons} seasons) \ngenres: {', ' .join(self.list_of_genre)}\nno ratings"
        return f"{self.title} ({self.number_of_seasons} seasons) \ngenres: {', '.join(self.list_of_genre)}\n{len(self.abc)} ratings, average {self.average():.1f} points"


    def rate(self,rating:int):
        self.abc.append(rating)

    def average(self):
        return sum(self.abc)/len(self.abc)


def minimum_grade(min,list):
    new=[]
    for items in list:
        if items.average()>=min:
            new.append(items)
    return new

def includes_genre(str,list):
    new=[]
    for items in list:
        for i in range(len(items.list_of_genre)):
            if str==items.list_of_genre[i]:
                new.append(items)
                break
    return new
if __name__=="__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    print(s1.average())
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    print(s2.average())
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series = [s1, s2, s3]
    print("a minimum grade of 4.5:")
    for series in minimum_grade(1.5, series):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series):
        print(series.title)
