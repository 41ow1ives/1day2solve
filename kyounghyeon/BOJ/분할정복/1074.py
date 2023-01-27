# 제목 : Z
# 분류 : 분할정복, Silver 1
# 출처 : 백준 1074

n, r, c = map(int, input().split())
cnt = 0
k = 2 ** n
while True:

    if k == 0:
        break

    if r < k // 2 and c < k // 2:  # 좌상단
        cnt += 0

    elif r < k // 2 and c >= k // 2:  # 우상단
        cnt += (k // 2) ** 2 * 1
        c -= k // 2

    elif r >= k // 2 and c < k // 2:  # 좌하단
        cnt += (k // 2) ** 2 * 2
        r -= k // 2

    elif r >= k //2 and c >= k // 2:  # 우하단
        cnt += (k // 2) ** 2 * 3
        r -= k // 2
        c -= k // 2

    k = k // 2

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)
