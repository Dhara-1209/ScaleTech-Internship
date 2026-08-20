def add(*number):
    sum=0
    for i in number:
        sum+=i
    return sum
    
def subtract(*number):
    diff=number[0]
    for i in number[1:]:
        diff-=i
    return diff

def division(*number):
    result = number[0]

    for i in number[1:]:
        if i == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= i

    return result

     
def multiple(*number):
    total=1
    for i in number:
        total*=i
    return total

def calculate(*number,operator):
    operation={
        "+": add,
        "-": subtract,
        "/": division,
        "*": multiple
    }

    if operator not in operation:
        raise ValueError(f"Unsupported operator: {operator}")
    
    return operation[operator](*number)
    
def main():
    print()
    print("*****    Simple CLI Calculator    *****")
    print(" Operators supported: +, -, *, / ")
    print("Type 'q' any time to exit or quit.\n")

    while True:
        user_input = input("Enter numbers separated by spaces: ")

        if user_input.lower() == "q":
            print()
            print("Goodbye!")
            break

        try:
            number = list(map(float, user_input.split()))

            operators=input("Enter operator (+, -, *, /):")

            result = calculate(*number, operator=operators)

            print("Result:",result)
            print()

        except ValueError as e:
            print(f"Invalid input: {e}\n")

        except ZeroDivisionError as e:
            print(f"Math error: {e}\n")


if __name__== "__main__":
        main()


