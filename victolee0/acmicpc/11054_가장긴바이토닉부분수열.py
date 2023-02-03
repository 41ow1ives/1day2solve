n = int(input())
nums = list(map(int, input().split()))
rnums = nums[::-1]
upper = [1] * n
lower = [1] * n

for end in range(n):
    for start in range(end):
        if nums[start] < nums[end]:
            upper[end] = max(upper[end], upper[start] + 1)
        if rnums[start] < rnums[end]:
            lower[end] = max(lower[end], lower[start] + 1)
        
result = [upper[i] + lower[n - i - 1] - 1 for i in range(n)]
print(max(result))