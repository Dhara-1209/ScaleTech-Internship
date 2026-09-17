class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving context")

with MyContext():

    name = "Dhara"

    for i in range(3):
        print(i)

    print(name)

    x = 10 + 20

    x=10/0
    print("Error")

    print(x)