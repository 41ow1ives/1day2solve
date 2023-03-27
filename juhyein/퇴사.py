# 이취코 풀이
# 뒤쪽부터 매 상담에 대하여 현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i]+i] 계산
# dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
# 점화식 : dp[i] = max(p[i] + dp[t[i]+i]], max_value) (max_value : 뒤에서부터 계산할 때 현재까지의 최대 상담 금액)
n = int(input());t = [] ; p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
   x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
for i in range(n-1, -1, -1):
  time = t[i]+i
  
  # 상담이 기간 안에 끝나는 경우
  if time <= n:
    dp[i] = max(p[i]+dp[time], max_value)
    max_value = dp[i]
    
  else:
    dp[i] = max_value
 
print(max_value)

 
