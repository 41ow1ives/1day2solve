import sys
si = sys.stdin.readline
n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]

arr.sort()
room = []

for s, e in arr:
    assigned = False
    for i in range(len(room)):
        if room[i] <= s:
            room[i] = e
            assigned = True
            break
        
    if not assigned:
        room.append(e)
        
print(len(room))