T=int(input())
for i in range(T):
    R,C=map(int,input().split(" "))
    L = [input().rstrip('\n') for _ in range(R)]
    print(f"Test {i+1}")
    for r in range(R - 1, -1, -1):
        print(L[r][::-1])