class ShoppingCart:
    def __init__(self, list1):
        self.list1=list1

    def __len__(self):
        return len(self.list1)

class Marks:
    def __init__(self,math,science):
        self.math=math
        self.science=science

    def __add__(self, other):
        return Marks(
            self.math + other.math,
            self.science + other.science
        )

    def __str__(self):
        return f"Maths: {self.math}, Science: {self.science}"


l1=ShoppingCart(["cold drinks","chips","biscuits","combs"])
print(len(l1))

m1=Marks(89,90)
m2=Marks(56,98)
m3=m1+m2
print(m3)