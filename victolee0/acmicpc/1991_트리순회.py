import sys
si = sys.stdin.readline
n = int(si())
child = [[-1, -1] for _ in range(n)]

for _ in range(n):
    par, x, y = si().split()
    idx = ord(par)-ord("A")
    child[idx][0] = x
    child[idx][1] = y

def preorder(x):
    if x == '.':
        return
    idx = ord(x)-ord('A')
    print(x, end='')
    preorder(child[idx][0])
    preorder(child[idx][1])

def inorder(x):
    if x == '.':
        return
    idx = ord(x)-ord('A')
    inorder(child[idx][0])
    print(x, end='')
    inorder(child[idx][1])
    
def postorder(x):
    if x == '.':
        return
    idx = ord(x)-ord('A')
    postorder(child[idx][0])
    postorder(child[idx][1])
    print(x, end='')
    
preorder('A')
print()
inorder('A')
print()
postorder('A')