try:
    a=int(input("enter number:"))
    result=10/a
except ValueError:
    print("Enter correct valid number")
except ZeroDivisionError:
    print("Enter other number than 0")
else:
    print(f"Result is {result}")
finally:
    print("done")
