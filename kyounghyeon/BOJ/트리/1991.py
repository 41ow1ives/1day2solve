# 제목 : 트리 순회
# 분류 : 트리 / Silver 1
# 출처 : 백준 1991

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]


def preorder(root, tree):
    print(root, end='')
    if tree[root][0] != ".":
        preorder(tree[root][0], tree)
    if tree[root][1] != ".":
        preorder(tree[root][1], tree)


def inorder(root, tree):
    if tree[root][0] != ".":
        inorder(tree[root][0], tree)
    print(root, end='')
    if tree[root][1] != ".":
        inorder(tree[root][1], tree)


def postorder(root, tree):
    if tree[root][0] != ".":
        postorder(tree[root][0], tree)
    if tree[root][1] != ".":
        postorder(tree[root][1], tree)
    print(root, end='')

preorder('A', tree)
print()
inorder('A', tree)
print()
postorder('A', tree)
print()