# 제목 : 트리의 순회
# 분류 : 트리, 재귀, 분할정복 / Gold 2
# 출처 : 백준 2263

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node_idx = [0] * (n+1)
# node_idx[x] = i : 노드 x의 index는 i
for i in range(n):
    node_idx[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]

    # left child
    preorder(in_start, node_idx[root]-1, post_start, post_start + node_idx[root] - 1)
    # right child
    preorder(node_idx[root]+1, in_end, node_idx[root], post_end-1)



preorder(0, n-1, 0, n-1)