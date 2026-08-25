class Students:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def get_average(self):
        total=self.marks1+self.marks2+self.marks3
        average=total/3
        print(f"Students name :{self.name}")
        print(f"Average ={average}")


s1=Students("Dhara",89,90,88)
s1.get_average()