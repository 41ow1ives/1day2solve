# https://www.acmicpc.net/problem/11899
# 괄호 끼워넣기 (SILVER III)

import sys

string = sys.stdin.readline().rstrip()
stack = []

for s in string:  # 모든 문자열을 돌면서
    stack.append(s)  # 일단 stack에 집어 넣음
    if s == ")" and len(stack) != 1:  # 만약 이번 문자열이 )이고 앞에 다른 확인할게 있다면?
        cur = stack.pop()
        check = stack.pop()
        if check != "(":  # 그런데 이번 문자열 ")"의 앞에 있는게 ")"라면 둘 다 다시 집어넣어준다.
            stack.extend([check, cur])

print(len(stack))  # 남아있는 개수만큼 짝 지어줘야함
