n = int(input())
num = list(map(int, input().split()))
x = int(input())
cnt = 0
num.sort()
i,j = 0,n-1

while i < j:
    if num[i]+num[j] == x:
        cnt += 1 ; i += 1 ; j -= 1
    elif num[i]+num[j] > x :
        j -= 1
    else:
        i += 1
        
print(cnt)
