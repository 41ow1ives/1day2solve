# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

stack = []
next_input = input()

while next_input != ".":
    for c in next_input:
        if c in ["(", "[", ")", "]"]:
            stack.append(c)
        if c == ")" and len(stack) != 1:
            if stack[-2] == "(":
                stack.pop()
                stack.pop()
        elif c == "]" and len(stack) != 1:
            if stack[-2] == "[":
                stack.pop()
                stack.pop()
    if stack:
        print("no")
    else:
        print("yes")
    stack = []
    next_input = input()
