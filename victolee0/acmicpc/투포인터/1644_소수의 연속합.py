import math

n = int(input())

p_nums = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if p_nums[i]:
        for j in range(i+i, n + 1, i):
            p_nums[j] = False
p_nums = [i for i in range(2, n + 1) if p_nums[i]]
                
R, ans, tmp = -1, 0, 0
len_p = len(p_nums)
for L in range(len_p):
    while R + 1 < len_p and tmp < n:
        tmp += p_nums[R + 1]
        R += 1
        
    if tmp == n:
        ans += 1
    tmp -= p_nums[L]

print(ans)