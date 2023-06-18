import sys
input = sys.stdin.readline
def min_init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        tree[node] = min(min_init(a, tree, node*2, start, (start+end)//2),
                         min_init(a, tree, node*2+1, (start+end)//2+1, end))
    return tree[node]

def max_init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        tree[node] = max(max_init(a, tree, node*2, start, (start+end)//2),
                         max_init(a, tree, node*2+1, (start+end)//2+1, end))
    return tree[node]

def min_query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1e+9
    if left <= start and end <= right:
        return tree[node]
    l = min_query(tree, node*2, start, (start+end)//2, left, right)
    r = min_query(tree, node*2+1, (start+end)//2+1, end, left, right)

    return min(l,r)

def max_query(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    l = max_query(tree, node*2, start, (start+end)//2, left, right)
    r = max_query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return max(l,r)

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]


min_tree = [-1] * 4 * n
max_tree = [-1] * 4 * n

min_init(a, min_tree, 1, 0, n-1)
max_init(a, max_tree, 1, 0, n-1)

for _ in range(m):
    left, right = map(int, input().split())
    min_ans = min_query(min_tree, 1, 0, n-1, left-1, right-1)
    max_ans = max_query(max_tree, 1, 0, n-1, left-1, right-1)
    print(min_ans, max_ans)
