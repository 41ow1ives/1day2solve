import sys
si = sys.stdin.readline
n, k = map(int, si().split())
nums = list(map(int, si().split()))

R = k
tmp = sum(nums[0:R])
ans = tmp
for L in range(1, n):
    R = L + k - 1
    if R >= n:
        continue
    tmp = tmp - nums[L - 1] + nums[R]

    if tmp > ans:
        ans = tmp

print(ans)