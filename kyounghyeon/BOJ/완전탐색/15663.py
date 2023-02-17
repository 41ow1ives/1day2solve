# 제목 : N과 M (9)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15663

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * (n+1)
lst = []

def find():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    before = 0
    for i in range(n):
        if not visited[i] and before != num[i]:
            lst.append(num[i])
            visited[i] = True
            before = num[i]
            find()
            lst.pop()
            visited[i] = False

find()