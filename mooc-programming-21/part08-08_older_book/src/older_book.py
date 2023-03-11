# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year


def older_book(a,b):
    if a.year==b.year:
        print(f"{a.name} and {b.name} were published in {a.year}")
    elif a.year<b.year:
        print(f"{a.name} is older, it was published in {a.year}")
    else:
        print(f"{b.name} is older, it was published in {b.year}")
# -----------------------------
# Write your solution here
# -----------------------------
if __name__=="__main__":
    python=Book("Fluent Python","Luciano Ramalho","programming",2015)
    everest=Book("High Adventure","Edmund Hillary","autobiography",1956)
    norma=Book("Norma","Sofi oksanen","crime",2015)

    older_book(python,everest)
    older_book(python,norma)