# TEE RATKAISUSI TÄHÄN:
class SimpleDate:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self,another:"SimpleDate"):
        if self.year==another.year:
            if self.month==another.month:
                if self.day==another.day:
                    return True
        return False

    def __ne__(self,another:"SimpleDate"):
        if self.year==another.year:
            if self.month==another.month:
                if self.day==another.day:
                    return False
        return True

    def __lt__(self,another:"SimpleDate"):
        if self.year==another.year:
            if self.month==another.month:
                if self.day<another.day:
                    return True
            elif self.month<another.month:
                return True
        elif self.year<another.year:
            return True
        return False
 
    def __gt__(self,another:"SimpleDate"):
        if self.year==another.year:
            if self.month==another.month:
                if self.day>another.day:
                    return True
            elif self.month>another.month:
                return True
        elif self.year>another.year:
            return True
        return False

    def __add__(self,number):
        x=self
        x.day+=number
        while x.day>30:
            x.day=x.day-30
            x.month+=1
        while x.month>12:
            x.month=x.month-12
            x.year+=1
        return x

    def __sub__(self,another:"SimpleDate"):
        if self.year==another.year:
            if self.month==another.month:
                if self.day>another.day:
                    return self.day-another.day
                else:
                    return another.day-self.day
            elif self.month>another.month:
                x=self.month-another.month
                y=self.day-another.day
                return x*30+y
            else:
                x=another.month-self.month
                y=another.day-self.day
                return x*30+y
        elif self.year>another.year:
            x=self.month-another.month
            y=self.day-another.day
            z=self.year-another.year
            return x*30+y+z*360
        else:
            x=another.month-self.month
            y=another.day-self.day
            z=another.year-self.year
            return x*30+y+z*360
    
if __name__=="__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)