# 제목 : 쿼드트리
# 분류 : 분할정복/재귀, Silver 1
# 출처 : 백준 1992

n = int(input())
video = []
for _ in range(n):
    video.append(list(map(int, input())))

def quad(x,y,n):

    num = video[x][y]
    same = True

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != video[i][j]:
                same = False
                break

    if not same:
        print("(", end="")
        quad(x, y, n // 2)
        quad(x, y + n // 2, n // 2)
        quad(x + n // 2, y, n // 2)
        quad(x + n // 2, y + n // 2, n // 2)
        print(")", end="")

    elif same:
        print(num, end="")

quad(0,0,n)





