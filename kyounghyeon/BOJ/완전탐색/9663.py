# 제목 : N-Queen
# 분류 : 완전탐색/백트래킹, Gold 4
# 출처 : 백준 9663

n = int(input())
chess = [0 for _ in range(n)]
cnt = 0
visited = [False] * n

def possible(row):  # row행 col열에 퀸을 둘 경우
    for k in range(row):  # row행보다 작은 행들에 대해 (이미 퀸이 있는 행에 대해)
        if row - k == abs(chess[row] - chess[k]):
            return False
    return True

def dfs(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]: continue  # i열은 이미 있으므로 pass

        chess[row] = i
        if possible(row):
            visited[i] = True
            dfs(row + 1)
            visited[i] = False

dfs(0)
print(cnt)