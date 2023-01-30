# 이취코 197pg 문제 풀이
# 매장의 N개 부품 중 손님이 요청한 M개의 부품 번호를 확인해 있으면 yes, 없으면 no 출력

# 1) 이진 탐색을 이용
N = int(input()) ; array = sorted(list(map(int, input().split())))
M = int(input()) ; m_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid]==target:
      return mid
    
    elif array[mid] > target:
      end = mid-1
     
    else:
      start = mid + 1
     
    return None

for target in m_list:
  result = binary_search(array, target, 0, N-1)
  if result != None:
    print('yes', end=' ' )
  else :
    print('no', end=' ')
   
  
  
# 2) 계수 정렬
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤, 리스트의 인덱스에 직접 접근하여 특정한 번호의 부품이 매장에 존재하는지 확인
n = int(input())
array = [0]*1000001

for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
    
# 3) 집합 자료형
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')











