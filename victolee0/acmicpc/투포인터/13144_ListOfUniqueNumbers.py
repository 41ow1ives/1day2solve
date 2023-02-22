import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))
visited = [0] * 1000001
ans = 0
R = -1
for L in range(n):
    while R + 1 < n and visited[nums[R + 1]] == 0:
        visited[nums[R + 1]] += 1
        R += 1
    ans += R - L + 1
    visited[nums[L]] -= 1

print(ans)