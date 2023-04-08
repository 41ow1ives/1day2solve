import sys
si = sys.stdin.readline
n = int(si())
A = list(map(int, si().split()))
memo = [0]
def bin_search(x):
    L, R = 0, len(memo) - 1
    
    while L <= R:
        mid = (L + R) // 2
        if memo[mid] < x:
            L = mid + 1
        else:
            R = mid - 1
    return L

for i in range(n):
    if memo[-1] < A[i]:
        memo.append(A[i])
    else:
        idx = bin_search(A[i])
        memo[idx] = A[i]

print(len(memo) - 1)
