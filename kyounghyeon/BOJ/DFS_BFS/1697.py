# 제목 : 숨바꼭질
# 분류 : 그래프 탐색, Silver 1
# 출처 : 백준 1697

from collections import deque

n, k = map(int, input().split())

def bfs(v):
    q = deque([v])
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        case = [x-1, x+1, 2*x]
        for w in case:
            if 0 <= w <= 100000 and not visited[w]:
                visited[w] = visited[x] + 1
                q.append(w)

visited = [0 for _ in range(100001)]
print(bfs(n))