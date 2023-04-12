n = int(input())
nums = sorted(list(map(int, input().split())))

def lower_bound(x, L):
    R = len(nums) - 1
    res = R
    while L < R:
        mid = (L + R) // 2
        if nums[mid] >= x:
            res = mid
            R = mid - 1
        else:
            L = mid + 1
    return res
    
val = 2e9

for i in range(n - 1):
    idx = lower_bound(-nums[i], i + 1)
    if i < idx - 1 < n and val > abs(nums[i] + nums[idx - 1]):
        val = abs(nums[i] + nums[idx - 1])
        v1, v2 = nums[i], nums[idx - 1]
        
    if i < idx < n and val > abs(nums[i] + nums[idx]):
        val = abs(nums[i] + nums[idx])
        v1, v2 = nums[i], nums[idx]

print(v1, v2)
