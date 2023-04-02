import sys
si = sys.stdin.readline
t = int(si())
for _ in range(t):
    p = si().strip()
    n = int(si())
    inp = si().strip()
    x = inp[1:-1].split(',')
    error = False
    cnt = 0

    for i in range(len(p)):
        if p[i] == 'R':
            cnt += 1
        elif p[i] == 'D':
            if n > 0:
                if cnt % 2 == 1:
                    x.pop()
                else:
                    x.pop(0)
                n -= 1
            else:
                error = True
                break
    if error:
        print("error")
    else:
        if cnt % 2 == 1:
            x = x[::-1]
        print(f'[{",".join(x)}]')