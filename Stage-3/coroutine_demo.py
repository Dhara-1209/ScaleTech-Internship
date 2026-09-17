def greet():
    print("Coroutine started")

    while True:
        name=yield
        print("Hello",name)

g= greet()
next(g)

g.send("Dhara")
g.send("Tanisha")

g.close()