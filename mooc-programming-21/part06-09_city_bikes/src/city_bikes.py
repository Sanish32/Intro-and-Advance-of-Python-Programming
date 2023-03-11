# Write your solution here
import math
def get_station_data(file:str):
    stations={}
    with open(file) as new_file:
        for line in new_file:
            line=line.strip()
            words=line.split(";")
            if words[0]=="Longitude":
                continue
            stations[words[3]]=(float(words[0]),float(words[1]))
    return stations

def distance(stations:dict,sta1:str,sta2:str):
    for key,value in stations.items():
        if key==sta1:
            longitude1=float(value[0])
            latitude1=float(value[1])
        if key==sta2:
            longitude2=float(value[0])
            latitude2=float(value[1])
    x=(longitude1-longitude2)*55.26
    y=(latitude1-latitude2)*111.2
    dist=math.sqrt(x**2 + y**2)
    return dist

def greatest_distance(stations:dict):
    sta1=""
    sta2=""
    far=0
    for key,value in stations.items():
        long1=value[0]
        lati1=value[1]
        for key2,value2 in stations.items():
            if key!=key2:
                long2=value2[0]
                lati2=value2[1]
                x=(long1-long2)*55.26
                y=(lati1-lati2)*111.2
                d=math.sqrt(x**2 + y**2)
                if d<0:
                    d*=-1
                if far<d:
                    far=d
                    sta1=key
                    sta2=key2
    return sta1,sta2,far

if __name__=="__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)