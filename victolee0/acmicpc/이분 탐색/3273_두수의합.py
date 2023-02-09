n = int(input())
nums = list(map(int, input().split()))
x = int(input())

def bin_search(lst, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return True
        if lst[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
            
    return False
        
nums.sort()
ans = 0
for i in range(n - 1):
    if bin_search(nums, i + 1, n - 1, x - nums[i]):
        ans += 1
       
print(ans) 
        