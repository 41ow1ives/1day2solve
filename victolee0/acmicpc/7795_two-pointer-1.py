import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    
    a.sort()
    b.sort()
    b.append(sys.maxsize)
    
    cnt = 0
    idx = 0
    for i, val1 in enumerate(a):
        
        if idx < m:    
            while val1 > b[idx]:
                idx += 1
            
        cnt += idx
            
    print(cnt)
