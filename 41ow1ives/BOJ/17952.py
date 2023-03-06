# https://www.acmicpc.net/problem/17952
# 과제는 끝나지 않아1 (SILVER III)

import sys

n = int(sys.stdin.readline())
stack_score, stack_num = [], []
answer = 0

for _ in range(n):
    cur = sys.stdin.readline().rstrip()

    if cur != '0':
        _, score, minute = list(map(int, cur.split()))
        if minute - 1 == 0:
            answer += score
        else:
            stack_score.append(score)
            stack_num.append(minute - 1)
    if cur == '0' and len(stack_num) > 0:  # 만약 비어있는 상태에서 0이 계속 들어오면 에러 나기 때문에 길이 조건 추가
        stack_num[-1] -= 1
        if stack_num[-1] == 0:
            stack_num.pop()
            answer += stack_score.pop()
print(answer)
"""
###### 더 나은 답:list를 굳이 두개 만들어둘 필요 없이 리스트 안의 리스트로 인덱싱해도 됨
import sys
input = sys.stdin.readline

n = int(input())
stack = []
score = 0
for _ in range(n):
    isTask, *task = map(int, input().split())
    if isTask == 1:
        stack.append(task)
        stack[-1][1] -= 1
    elif isTask == 0:
        if stack:
            stack[-1][1] -= 1
    if stack:
        if stack[-1][1] == 0:
            score += stack.pop()[0]
print(score)

"""
"""
###### 메모리 초과 -> score를 횟수만큼 저장해둘 필요가 없음!
import sys

n = int(sys.stdin.readline())
stack_score, stack_num = [], []
answer = 0

for _ in range(n):
    cur = sys.stdin.readline().rstrip()

    if cur != '0':
        _, score, minute = list(map(int, cur.split()))
        if minute - 1 == 0:
            answer += score
        else:
            stack_score.extend([score] * (minute - 1))
            stack_num.append(minute)
    else:
        tmp = stack_score.pop()
        stack_num[-1] -= 1
        if stack_num[-1] == 1:
            stack_num.pop()
            answer += tmp

print(answer)
"""

"""
for _ in range(n):
    cur = sys.stdin.readline().rstrip()
    if cur != '0':
        _, score, min = map(int, cur.split())
        if min - 1 == 0:  # 1분만에 끝나는 과제라면 바로 점수 추가
            answer += score
        else:  # 그렇지 않다면 이번 시간을 제외하고 그 횟수만큼 stack에 쌓아준다.
            stack.extend([score] * (min - 1))
    else:
        tmp = stack.pop()
        if len(stack) != 0 and tmp != stack[-1]:  # 이렇게 하면 점수가 똑같은게 등장했을 때 에러 남
            answer += tmp
        if len(stack) == 0:
            answer += tmp
print(answer)

"""
