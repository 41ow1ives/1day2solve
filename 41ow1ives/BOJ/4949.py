# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

stack = []
next_input = input()

while next_input != ".":
    for chr in next_input:
        if chr in ["(", "[", ")", "]"]:
            stack.append(chr)
        if chr == ")" and len(stack) != 1:
            if stack[-2] == "(":
                stack.pop()
                stack.pop()
        elif chr == "]" and len(stack) != 1:
            if stack[-2] == "[":
                stack.pop()
                stack.pop()
    if stack:
        print("no")
    else:
        print("yes")
    stack = []
    next_input = input()
