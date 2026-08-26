class Canswim:
    def swim(self):
        print("Swimming")

class Canfly:
    def fly(self):
        print("Flying")

class Brid(Canfly):
    def caneat(self):
        print("Eating")
class duck(Canfly,Canswim):
    pass
b1=Brid()
b1.fly()
b1.caneat()
d1=duck()
d1.fly()
d1.swim()

