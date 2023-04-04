import sys
si = sys.stdin.readline
n = int(si())
img = [si().strip() for _ in range(n)]

ans = ''
def func(x, y, length):
    global ans
    prev = img[x][y]
    possible = True
    for i in range(length):
        for j in range(length):
            if img[x + i][y + j] != prev:
                possible = False
                ans += '('
                func(x, y, length // 2)
                func(x, y + length // 2, length // 2)
                func(x + length // 2, y, length // 2)
                func(x + length // 2, y + length // 2, length // 2)
                ans += ')'
                return
    if possible:
        ans += str(prev)
    
    
    
func(0, 0, n)
print(ans)