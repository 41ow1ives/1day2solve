# 제목 : 트리의 순회
# 분류 : 트리, 재귀, 분할정복 / Gold 2
# 출처 : 백준 2263

import sys
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# .index()로 인한 시간초과가 발생하지 않도록 각 노드의 inorder 인덱스 저장
node_idx = [0] * (n+1)
for i, node in enumerate(inorder):
    node_idx[node] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    root_idx = node_idx[root]
    print(root, end=' ')

    # left child
    preorder(in_start, root_idx-1, post_start, post_start + root_idx - in_start - 1)
    # right child
    preorder(root_idx+1, in_end, root_idx - in_end + post_end, post_end-1)

preorder(0, n-1, 0, n-1)