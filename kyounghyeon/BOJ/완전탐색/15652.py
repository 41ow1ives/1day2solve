# 제목 : N과 M (4)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15652

n, m = map(int, input().split())
ans = []

def H(x):

    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(x, n+1):
        ans.append(i)
        H(i)
        ans.pop()

H(1)