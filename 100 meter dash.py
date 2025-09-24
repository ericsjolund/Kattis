import math

a = int(input())
points = []
points = [(0.0, 0.0, 0.0)] + points

for _ in range(a):
    x, y, t = map(float, input().split(" "))
    points.append((x, y, t))

segs = []

ans = float("inf")
eps = 1e-12

for i in range(1, len(points)):
    x0, y0, t0 = points[i - 1]
    x1, y1, t1 = points[i]

    l = math.hypot(x1 - x0, y1 - y0)
    dt = t1 - t0

    if dt <= 0:
        continue
    v = l / dt
    segs.append((l, dt, v))

    if i == 1:
        lwin = 0.0
        twin = 0.0
        s = 0

    for e, (l, dt, v) in enumerate(segs[-1:], start=len(segs)-1):
        lwin += l
        twin += dt

        while s <= e and lwin - segs[s][0] >= 100 - eps:
            lwin -= segs[s][0]
            twin -= segs[s][1]
            s += 1

        lbl = lwin - l
        tbl = twin - dt
        n = 100 - lbl

        if n > 0:
            t_take = min(n, l)
            if t_take >= n - eps:
                ans = min(ans, tbl + t_take / v)

        if lwin >= 100 - eps:
            surp = lwin - 100
            vstart = segs[s][2]
            ans = min(ans, twin - surp / vstart)

print(ans, flush=True)