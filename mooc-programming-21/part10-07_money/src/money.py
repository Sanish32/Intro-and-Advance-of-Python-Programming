# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        if self.__cents<10:
            self.__total=str(self.__euros)+(".0")+str(self.__cents)
            self.__total=float(self.__total)
        else:
            self.__total=self.__euros+(self.__cents/100)
    def __str__(self):
        if self.__cents<10:
            return f"{self.__euros}.0{self.__cents} eur"
        else:
            return f"{self.__euros}.{self.__cents} eur"
        
    def __eq__(self,another:"Money"):
        if self.__euros==another.__euros:
            if self.__cents==another.__cents:
                return True
        return False

    def __gt__(self,another:"Money"):
        return self.__total>another.__total

    def __lt__(self,another:"Money"):
        return self.__total<another.__total

    def __ne__(self,another:"Money"):
        return self.__total!=another.__total

    def __add__(self,another:"Money"):
        return f"{self.__total+another.__total:.2f} eur"


    def __sub__(self,another:"Money"):
        if self.__total-another.__total<0:
            raise ValueError("a negative result is not allowed")
        return f"{self.__total-another.__total:.2f} eur"
        
if __name__=="__main__":
    e1=Money(4,5)
    print(e1)
    e1.euros=1000
    print(e1)