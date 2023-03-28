# 제목 : 문서 검색
# 분류 : 완탐, Silver 4
# 출처 : 백준 1543

full = input()
find = input()

cnt = 0
i = 0

while i+len(find) <= len(full):
    if full[i:(i+len(find))] == find:
        cnt += 1
        i += len(find)
    else:
        i += 1

print(cnt)