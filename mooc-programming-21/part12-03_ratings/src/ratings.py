# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items:list):
    def abc(item:dict):
        return item["rating"]
 
    d=sorted(items,key=abc)
    d.reverse()
    return d

if __name__=="__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")