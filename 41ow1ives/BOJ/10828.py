# https://www.acmicpc.net/problem/10828
# 스택
"""
input() 말고 sys.stdin.readline()을 이용해야 시간초과 X
"""


import sys

n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    input_ = sys.stdin.readline().split()
    order = input_[0]

    if order == "push":
        m = int(input_[1])
        answer.append(int(m))
    elif order == "top":
        print(answer[-1]) if bool(answer) == True else print(-1)
    elif order == "size":
        print(len(answer))
    elif order == "empty":
        print(0) if bool(answer) == True else print(1)
    elif order == "pop":
        print(answer.pop()) if bool(answer) == True else print(-1)
    else:
        ValueError("Not Implemented Order")
