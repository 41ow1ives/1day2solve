import sys
from collections import deque
si = sys.stdin.readline
h, k, r = map(int ,si().split())
Q = [[deque([]) for _ in range(2 ** (h + 1))] for _ in range(2)]


for i in range(2 ** h):
    Q[0][2 ** h + i] = deque(list(map(int, si().split())))

complete = []
for day in range(1, r + 1):
    left = day % 2 
    for x in range(1, 2 ** (h + 1)):
        possible = False
                
        if left and Q[0][x] and x < 2 ** h:
            n = Q[0][x].popleft()
            possible = True

        if not left and Q[1][x] and x < 2 ** h:
            n = Q[1][x].popleft()
            possible = True

        if x == 1 and possible:
            complete.append(n)

        if 1 < x < 2 ** h and possible:
            if x % 2:
                Q[1][x // 2].append(n)
            else:
                Q[0][x // 2].append(n)

        if x >= 2 ** h:
            if Q[0][x]:
                n = Q[0][x].popleft()
                if x % 2:
                    Q[1][x // 2].append(n)
                else:
                    Q[0][x // 2].append(n)

print(sum(complete))