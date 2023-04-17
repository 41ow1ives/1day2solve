import sys
si = sys.stdin.readline
n = int(si())

W = [list(map(int, si().split())) for _ in range(n)]
dist = [[0] * (1 << n) for _ in range(n)]
INF = int(1e6 * 16)
# visited는 N개의 비트를 십진수로 변환한 형태가 된다.
def dfs(x, visited):
    # 모든 정점을 방문한 경우 N개의 비트가 모두 1이 된다.
    # 그래서 (1 << n) - 1이면 탐색 종료
    if visited == (1 << n) - 1:
        if W[x][0] != 0:
            return W[x][0]
    # 마지막 방문이 x이면서 visited에 체크된 정점에 방문한 기록이 있는 경우
    if dist[x][visited]:
        return dist[x][visited]
    cost = INF
    # 0번째 정점부터 시작하기 때문에 1번 정점부터 순회
    # 정점을 순회하며
    for i in range(1, n):
        # not visited => visited의 i번째 비트가 0이고
        # => i번째 비트에 방문하지 않았으면서 
        # 현재 정점(x)에서 다음 정점(i)로 가는 경로의 가중치가 0이 아닌 경우
        if not visited & (1 << i) and W[x][i] != 0:
            # cost 업데이트
            # dfs(i번 정점에 방문한 경우, visited을 i번 정점에 방문한 것으로 수정)
            # 결과 값에 정점 x에서 i로 가는 가중치 추가
            cost = min(cost, dfs(i, visited | (1 << i)) + W[x][i])
            
    dist[x][visited] = cost
    return cost

ans = dfs(0, 1)
print(ans)