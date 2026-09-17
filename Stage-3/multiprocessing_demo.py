from multiprocessing import Process

def task(name):
    print("Running", name)

p1 = Process(target=task, args=("Task 1",))
p2 = Process(target=task, args=("Task 2",))

p1.start()
p2.start()

p1.join()
p2.join()

print("Done")