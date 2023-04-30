from collections import deque
K = int(input())
nums = deque([])
for _ in range(K):
    x = int(input())
    if x == 0:
        nums.pop()
    else:
        nums.append(x)
        
print(sum(nums))
