#Julmust

import sys

def main():
    line = sys.stdin.readline()
    if not line:
        return
    M = int(line.strip())

    lo, hi = 1, M
    t = 0
    while lo <= hi:
        t += 1
        q = (lo + hi) // 2
        X = t * q

        print(X, flush=True)

        ans = sys.stdin.readline()
        if not ans:
            return  
        ans = ans.strip()

        if ans == "exact":
            return 
        elif ans == "less":
            hi = q - 1
        elif ans == "more":
            lo = q + 1
        else:
            return

if __name__ == "__main__":
    main()