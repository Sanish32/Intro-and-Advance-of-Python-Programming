# Write your solution here:
class Task:
    id=0
    
    def __init__(self,description,programmer,workload):
        self.description=description
        self.programmer=programmer
        self.workload=workload
        self.field=False
        Task.id+=1
        self.id=Task.id

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.is_finished() else 'NOT FINISHED'}"

    def is_finished(self):
        return self.field

    def mark_finished(self):
        self.field=True


class OrderBook(Task):
    def __init__(self):
        self.order=[]

    def add_order(self,description, programmer, workload):
        abc=Task(description,programmer,workload)
        self.order.append(abc)

    def all_orders(self):
        return list([item for item in self.order])

    def programmers(self):
        return list(set([item.programmer for item in self.order]))

    def mark_finished(self,id:int):
        a=False
        for item in self.order:
            if id==item.id:
                item.mark_finished()
                a=True
        if not a:
            raise ValueError("")

    def finished_orders(self):
        return [item for item in self.order if item.field==True]


    def unfinished_orders(self):
        return [item for item in self.order if item.field==False]

    def status_of_programmer(self,string):
        a=False
        c1=0
        c2=0
        c3=0
        c4=0
        for item in self.order:
            if string==item.programmer:
                if item.is_finished()==True:
                    c1+=1
                    c3+=item.workload
                else:
                    c2+=1
                    c4+=item.workload
                a=True
        if not a:
            raise ValueError("")
        return (c1,c2,c3,c4)

if __name__=="__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
