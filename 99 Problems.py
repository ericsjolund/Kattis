a=int(input())
l = a
u = a
while True:
    if int(str(u)[-2:]) == 99:
        t=False
        print(u)
        break
    elif int(str(l)[-2:]) == 99:
        t=False
        print(l)
        break
    else:
        l-=1
        u+=1