N = int(input())
video = []
for _ in range(N):
		video.append(input())
ans = []
def DC(x,y,n):
    global ans
    num = video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != video[i][j]:
                ans.append("(")
                DC(x,y,n//2)
                DC(x, y+n//2, n//2)
                DC(x+n//2, y, n//2)
                DC(x+n//2, y+n//2, n//2)
                ans.append(")")
    ans.append(num)

DC(0,0,N)
print("".join(ans))