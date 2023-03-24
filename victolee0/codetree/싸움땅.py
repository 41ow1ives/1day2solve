import sys
si = sys.stdin.readline

n, m, k = map(int, si().split())
guns = [list(map(int, si().split())) for _ in range(n)]
players = []
players_loc = [[-1] * n for _ in range(n)]

for i in range(m):
    x, y, d, s = map(int, si().split())
    players.append([x - 1, y - 1, d, s, 0])
    #players_loc[x][y] = i

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def move(x, y, d):
    if x + dx[d] < 0 or x + dx[d] >= n or y + dy[d] < 0 or y + dy[d] >= n:
        d = (d + 2) % 4
    x = x + dx[d]
    y = y + dy[d]
    return x, y, d

def is_player(x, y):
    #if players_loc[x][y] == -1:
    #    return False
    for i, player in enumerate(players):
        if x == player[0] and y == player[1]:
            return i
    return -1

def get_gun(x, y, g):
    if guns[x][y] == 0:
        return g

    if type(guns[x][y]) == int:
        val = max(g, guns[x][y])
        guns[x][y] = min(g, guns[x][y])
        return val
    else:
        tmp = guns[x][y] + [g]
        val = max(tmp)
        tmp.remove(val)
        guns[x][y] = tmp
        return val

def battle(player1, player2):
    stat1 = player1[3] + player1[4]
    stat2 = player2[3] + player2[4]
    if stat1 > stat2:
        return 0, stat1 - stat2
    elif stat1 < stat2:
        return 1, stat2 - stat1
    else:
        if player1[3] > player2[3]:
            return 0, 0
        else:
            return 1, 0
    #NoneType err

def lose_act(player):
    x, y, d, s, g = player
    if type(guns[x][y]) == int:
        guns[x][y] = [guns[x][y], g]
    else:
        guns[x][y].append(g)
    g = 0

    while x + dx[d] < 0 or x + dx[d] >= n or y + dy[d] < 0 or y + dy[d] >= n or is_player(x + dx[d], y + dy[d]) != -1:
        d = (d + 1) % 4
    x = x + dx[d]
    y = y + dy[d]

    g = get_gun(x, y, g)

    return [x, y, d, s, g]

def win_act(player):
    x, y, d, s, g = player
    g = get_gun(x, y, g)
    return [x, y, d, s, g]

points = [0] * m
for _ in range(k):
    for i in range(m):
        x, y, d, s, g = players[i]
        x, y, d = move(x, y, d)
        b = is_player(x, y)
        if b != -1:
            players[i] = [x, y, d, s, g]
            winner, point = battle(players[i], players[b])
            win_p = i if winner == 0 else b
            lose_p = b if winner == 0 else i
            points[win_p] += point
            players[lose_p] = lose_act(players[lose_p])
            players[win_p] = win_act(players[win_p])

        else:
            g = get_gun(x, y, g)
            players[i] = [x, y, d, s, g]
        

print(' '.join(str(i) for i in points))