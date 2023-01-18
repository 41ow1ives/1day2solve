import sys

n = int(input())

dp = []
for _ in range(n):
    costs = list(map(int, sys.stdin.readline().split()))
    if not dp:
        tmp = []
        for i in range(3):
            tmp.append([costs[i], i])
        dp = [tmp]
    else:
        tmp = []
        prev = dp[-1]
        for i in range(3):        
            val = [1e+9, -1]
            for prev_cost, prev_color in prev:
                if prev_color != i:
                    tmp_val = prev_cost + costs[i]
                    if val[0] > tmp_val:
                        val = [tmp_val, i]
            tmp.append(val)
        dp = [tmp]
                
res = [i[0] for i in dp[-1]]
print(min(res))
            

