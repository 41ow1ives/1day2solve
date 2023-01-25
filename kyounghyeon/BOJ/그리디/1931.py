# 제목 : 회의실 배정
# 분류 : 그리디, Silver 1
# 출처 : 백준 1931

import sys

n = int(input())
meeting = [[0] * 2 for _ in range(n)]

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting[i][0] = s
    meeting[i][1] = e

meeting.sort(key = lambda x: (x[1], x[0])) # 끝나는 시각이 빠른 순, 회의 시간이 짧은 순
# key의 두 번쨰 element를 x[1] - x[0] (회의 시간)으로 해버리면, 시작 시간 = 끝나는 시간 인 경우에 대처 불가

cnt = 0
e = 0
for m in meeting:
    if e <= m[0]:
        cnt += 1
        e = m[1]

print(cnt)
