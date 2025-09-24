board = [list(map(int, input().split())) for _ in range(4)]
d = int(input())



def move_left(row):
    tiles = [x for x in row if x != 0]
    out = []
    i = 0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            out.append(tiles[i] * 2)
            i += 2 
        else:
            out.append(tiles[i])
            i += 1

    out += [0] * (4 - len(out))
    return out

def transpose(g):
    return [list(x) for x in zip(*g)]

if d == 0:
    board = [move_left(row) for row in board]

elif d == 2:
    board = [list(reversed(move_left(list(reversed(row))))) for row in board]

elif d == 1:
    t = transpose(board)
    t = [move_left(row) for row in t]
    board = transpose(t)

elif d == 3:
    t = transpose(board)
    t = [list(reversed(move_left(list(reversed(row))))) for row in t]
    board = transpose(t)

for row in board:
    print(*row)