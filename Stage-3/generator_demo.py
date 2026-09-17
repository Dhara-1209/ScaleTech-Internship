def fun(n):
    num=1
    while num <=n:
        yield num
        num+=1

crt= fun(5)
for i in crt:
    print(i)
