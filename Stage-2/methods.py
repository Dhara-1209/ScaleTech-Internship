class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return f"{self.brand} {self.model} - ₹{self.price}"
        
    def showDetails(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

car1 = Car("Toyota", "Camry", 3000000) 
print(car1)
car1.showDetails()