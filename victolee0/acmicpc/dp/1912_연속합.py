import sys
si = sys.stdin.readline
n = int(si())
nums = list(map(int, si().split()))


ans = -1000 * 100000
prev = 0

for num in nums:

    prev = max(prev + num, num)
    ans = max(prev, ans)
    
print(ans)