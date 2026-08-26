class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(C,B):
    #pass
    def show(self):
        print("D")
        super().show()

d1=D()
d1.show()

                      