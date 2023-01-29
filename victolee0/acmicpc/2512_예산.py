n = int(input())
nums = list(map(int, input().split()))
m = int(input())

def func(x):
    val = 0
    for i in nums:
        val += min(x, i)
    return val <= m

low = 0
high = max(nums)
ans = 0

while low <= high:
    mid = (low + high) // 2
    if func(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(ans)
