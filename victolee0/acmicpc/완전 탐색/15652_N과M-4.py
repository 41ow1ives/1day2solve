n, m = map(int, input().split())

selected = [0 for _ in range(m)]
used = [1]
def rec_func(k):
    if k == m:
        out = ' '.join([str(i) for i in selected])
        print(out)
    else:
        for i in range(used[-1], n + 1):
            selected[k] = i
            used.append(i)
            rec_func(k + 1)
            selected[k] = 0
            used.pop()
            
rec_func(0)