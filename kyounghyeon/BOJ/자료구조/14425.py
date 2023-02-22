# 제목 : 문자열 집합
# 분류 : 자료구조, Silver 3
# 출처 : 백준 14425
import sys

n, m = map(int, input().split())
S, check= {}, []

for _ in range(n):
    abc = sys.stdin.readline()
    S[abc] = 1

cnt = 0
for _ in range(m):
    xyz = sys.stdin.readline()
    if xyz in S.keys():
        cnt += 1

print(cnt)
