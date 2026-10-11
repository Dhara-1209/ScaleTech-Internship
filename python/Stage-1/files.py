name=input("Enter name:")
age=int(input("Enter age:"))

with open("student.txt","a") as f:
    f.write(f"{name},{age}\n")

with open("student.txt","r") as f:
    line=f.readline()
    lines=f.readlines()
    print(line)
    print(lines)