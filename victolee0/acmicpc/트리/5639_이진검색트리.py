import sys
sys.setrecursionlimit(20000)
si = sys.stdin.readline

nums = []
while True:
    n = si()
    if not n:
        break
    if n == '\n':
        break
    nums.append(int(n))
    
def rec_func(l, r):
    if l > r:
        return
    mid = r
    for i in range(l + 1, r + 1):
        if nums[i] > nums[l]:
            mid = i - 1
            break
    rec_func(l + 1, mid)
    rec_func(mid + 1, r)
    
    print(nums[l])
    
rec_func(0, len(nums) - 1)