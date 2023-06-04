import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
p = [0] * (n+1)
for i in range(1,n+1):
    p[i]=(p[i-1] + nums[i-1])

for _ in range(m):
    a, b = map(int, input().split())
    print(p[b] - p[a-1])
