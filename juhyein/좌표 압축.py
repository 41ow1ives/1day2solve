import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = dict()
vals = sorted(list(set(arr)))
for i, val in enumerate(vals):
    d[val] = i
print(' '.join(str(d[a]) for a in arr))
