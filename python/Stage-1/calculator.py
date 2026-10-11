def add(*number):
    sum=0
    for i in number:
        sum+=i
    print(sum)
print("Calculator module loaded")

if __name__=="__main__":
    print(add(5,3))
    
def subtract(*number):
    diff=number[0]
    for i in number[1:]:
        diff-=i
    print(diff)

def divison(a,b):
    print(a/b)

def multiple(*number):
    total=1
    for i in number:
        total*=i
    print(total)

