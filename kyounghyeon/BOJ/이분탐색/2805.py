# 제목 : 나무 자르기
# 분류 : 이분탐색 , Silver 2
# 출처 : 백준 2805

n, m = map(int, input().split())
tree = list(map(int, input().split()))
low, high = 1, max(tree)

while low <= high:
    mid = (low + high) // 2

    total = 0
    for t in tree:
        if t >= mid:
            total += t - mid

    if total >= m:  # 넘치면 절단기 높이 올림
        low = mid + 1
    else:
        high = mid - 1

print(low)
