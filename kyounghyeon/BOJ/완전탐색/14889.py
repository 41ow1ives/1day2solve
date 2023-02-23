# 제목 : 스타트와 링크
# 분류 : 완전탐색/백트래킹, Silver 2
# 출처 : 백준 14889

'''백트래킹으로 구하기'''
import sys
input = sys.stdin.readline
n = int(input())
S = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
score = 1e9

def dfs(depth, idx):
    global score
    if depth == n // 2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += S[i][j]
                elif not visited[i] and visited[j]:
                    team2 += S[i][j]
        score = min(score, abs(team1-team2))
        return

    '''
    팀을 나누기 위한 for문
    팀이 반반이 되기까지는 점수 계산을 하지 않고, n명의 사람을 팀에 배정하는 구문만 수행함
    스타트팀은 visited == True, 링크팀은 vistited == False로 구분함.
    Ex) 0,1,2,3 (team1) ==> 점수 계산 ==> return 후 3을 팀에 넣기 직전 재귀문으로 back ==> 0,1,2,4 (team1) ==> 점수 계산 ... ==> 
    '''
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(score)