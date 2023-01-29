# 이취코 201pg 이진 탐색 연습문제
# 파라메트릭 서치
# key : 시작점은 0, 끝점은 가장 긴 떡의 길이

n,m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
  total = 0
  mid = (start + end)//2
  for x in array:
    # 잘랐을 때의 떡의 양 계산
    if x>mid:
      total += x - mid
    else:
      result = mid
      start = mid + 1
      
print(result)
