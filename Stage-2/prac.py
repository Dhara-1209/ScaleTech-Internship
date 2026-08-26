class Circle:
    def __init__(self,r):
        self.r=r

    def Area(self):
        return 3.14 *(self.r**2)

    def Perimeter(self):
        return 2 * 3.14 * self.r
        

c1=Circle(21)
print(c1.Area())
print(c1.Perimeter())