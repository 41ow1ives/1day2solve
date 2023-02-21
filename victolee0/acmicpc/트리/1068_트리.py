import sys
si = sys.stdin.readline

n = int(si())
parents = list(map(int, si().split()))
child = [[] for _ in range(n)]
remove = int(si())
leaf = [0] * n
root = 0
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        if remove == i:
            continue
        child[parents[i]].append(i)
        
def dfs(x):
    if not child[x]:
       leaf[x] = 1
    
    for y in child[x]:
        dfs(y, x)
        leaf[x] += leaf[y]
        
if remove != root:
    dfs(root)

print(leaf[root])