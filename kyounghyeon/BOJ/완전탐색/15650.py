# 제목 : N과 M (2)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15650

n, m = map(int, input().split())
ans = []
existed = [False] * n

def Comb(x):

    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(x, n+1):
        if existed[i]:
            continue

        ans.append(i)
        existed[i] = True
        Comb(i+1)
        ans.pop()
        existed[i] = False

Comb(1)
