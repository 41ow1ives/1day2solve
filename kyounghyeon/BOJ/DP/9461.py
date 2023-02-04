# 제목 : 파도반 수열
# 분류 : DP, Silver 3
# 출처 : 백준 9461

t = int(input())
P = [0,1,1,1,2,2]
for i in range(6, 101):
    P.append(P[i-1] + P[i-5])

for _ in range(t):
    print(P[int(input())])