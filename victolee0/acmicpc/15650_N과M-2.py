n, m = map(int, input().split())

selected = [0 for _ in range(m)]
used = []

def rec_func(k):
    if k == m:
        ans = ' '.join([str(i) for i in selected])
        print(ans)
    else:
        start = 0 if k == 0 else selected[k - 1]
        for i in range(start + 1, n + 1):
            selected[k] = i
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)