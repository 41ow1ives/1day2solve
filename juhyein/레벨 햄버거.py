# 레벨 N버거, 햄버거 아래 X장 패티 개수
# 레벨 0버거 - 패티만(P)
# 레벨 L버거 - B, 레벨 L-1, P, 레벨 L-1, B
N,X = map(int, input().split())

burger = ""
for i in range(N + 1):
  if i == 0 :
    burger = "P"
  else :
    burger = "B" + burger + "P" + burger + "B"

burger[0:X].count("P")
