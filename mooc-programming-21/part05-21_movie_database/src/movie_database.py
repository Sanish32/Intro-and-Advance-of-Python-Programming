# Write your solution here
def add_movie(db,name,director,year,runtime):
    groups={}
    db.append(groups)
    if name not in groups:
        groups["name"]=name
        groups["director"]=director
        groups["year"]=year
        groups["runtime"]=runtime 

if __name__=="__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)