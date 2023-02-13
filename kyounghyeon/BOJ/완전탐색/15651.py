# 제목 : N과 M (3)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15651

n, m = map(int, input().split())
ans = []

def H():

    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        ans.append(i)
        H()
        ans.pop()

H()
