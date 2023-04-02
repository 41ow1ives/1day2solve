import sys
si = sys.stdin.readline
n, m = map(int, si().split())
nums = sorted(list(map(int, si().split())))
selected = [0] * m
used = [0] * (n + 1)
def rec_func(k):
    if k == m:
        for x in selected:
            print(x, end=' ')
        print()
    else:
        prev = 0
        for x in range(n):
            if used[x] == 1 or nums[x] == prev:
                continue
            prev = nums[x]
            selected[k] = nums[x]
            used[x] = 1
            rec_func(k + 1)
            selected[k] = 0
            used[x] = 0
            
rec_func(0)