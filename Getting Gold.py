#Getting Gold
w, h = map(int, input().split())
grid = [list(input()) for _ in range(h)]


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for y in range(h):
    for x in range(w):
        if grid[y][x] == 'P':
            start = (x, y)

visited = [[False]*w for _ in range(h)]
queue = [start]
visited[start[1]][start[0]] = True
gold = 0

def is_adjacent_to_trap(x, y):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if grid[ny][nx] == 'T':
            return True
    return False

while queue:
    x, y = queue.pop(0)
    if grid[y][x] == 'G':
        gold += 1

    if is_adjacent_to_trap(x, y):
        continue

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not visited[ny][nx] and grid[ny][nx] != '#' and grid[ny][nx] != 'T':
            visited[ny][nx] = True
            queue.append((nx, ny))

print(gold)