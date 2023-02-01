from collections import deque

n, k = map(int, input().split())
min_t = abs(n - k)

if n >= k:
    print(n - k)
else:
    queue = deque([(k, 0)])
    visited = []
    while queue:
        now, t = queue.popleft()
        if now in visited:
            continue
        visited.append(now)
        if now == n:
            print(t)
            break
        elif now % 2 == 0:
            queue.append((now // 2, t + 1))
        
        queue.append((now + 1, t + 1))
        queue.append((now - 1, t + 1))
    