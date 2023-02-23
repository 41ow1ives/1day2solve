import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))
nums.sort()

def func(idx):
    L = 0
    R = n - 1
    while L < R:
        target = nums[idx]
        val = nums[L] + nums[R]
        if L == idx: L += 1
        elif R == idx: R -= 1
        else:
            if val < target:
                L += 1
            elif val > target:
                R -= 1
            else:
                return True
    return False

ans = [1 for i in range(n) if func(i)]
print(len(ans))