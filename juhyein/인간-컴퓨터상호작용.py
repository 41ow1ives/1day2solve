import sys
from collections import Counter
input = sys.stdin.readline

s = input()
q = int(input())
p = [0] * (len(s))

for i in range(len(s)):
    p[i] = Counter(s[:i+1])    

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    if l == 0:
        print(p[r][a])
    else:
        print(p[r][a] - p[l-1][a])
