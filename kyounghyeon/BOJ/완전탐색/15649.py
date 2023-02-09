# 제목 : N과 M (1)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15650

n, m = map(int, input().split())
ans = []

existed = [False] * (n+1)

def Perm():
    if len(ans) == m:
        print(' '. join(map(str, ans)))
        return

    for i in range(1, n+1):
        if existed[i]:
            continue
        ans.append(i)
        existed[i] = True
        Perm()
        ans.pop()
        existed[i] = False

Perm()