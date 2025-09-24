while True:
    total = 0
    y1 = 0
    c = int(input())
    if c != -1:
        for _ in range(c):
            x,y = map(int, input().split(" "))
            dy = y - y1
            total += x*dy 
            y1 = y
        print(total, "miles")
    else:
        break