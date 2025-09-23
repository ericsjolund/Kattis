#Klósettröð
n = int(input())
v = list(map(int, input().split(" ")))
e=[0]*n
pos = 0
for i in range(n):
    for j in range(len(v)):
        if v[j] == max(v):
            e[i] = j+1
            v[j] = 0
            break
print(' '.join(map(str, e)))