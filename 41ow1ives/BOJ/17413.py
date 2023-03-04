# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2 (Silver III)

####### 스택으로 접근
import sys

sentence = list(sys.stdin.readline().rstrip()) + [" "]
answer = []
tmp = ''
flag = False

for s in sentence:

    if flag:
        answer.append(s)
    else:
        if s == " ":  # 공백의 경우에는 포함이 되어야 함
            tmp = tmp[::-1]
            tmp += s
            answer.append(tmp)
            tmp = ''
        elif s == "<":  # 반면 <는 포함되면 안됨
            answer.append(tmp[::-1])
            tmp = ''
        else:
            tmp += s

    if s == "<":
        flag = True
        answer.append(s)
    elif s == ">":
        flag = False  # 맨 위에서 >는 append 해줬음

print("".join(answer))

"""
###### 구현으로 접근
import sys

sentence = list(sys.stdin.readline().rstrip()) + [
    " "
]  # 두번째 while에서 end_idx < len(sentence) 조건 안 넣기 위해서 추가
idx = 0

while idx < len(sentence):

    if sentence[idx] == "<":
        while sentence[idx] != ">":
            idx += 1
        idx += 1  # 닫힌 괄호를 만났으니 +1 (안 해주면 >에서 멈춰있으니까!)

    start_idx = idx
    end_idx = idx

    while sentence[end_idx] not in [" ", "<"]:  # 마지막에 공백 넣어줬으므로 태그로 끝나도 다음 글자가 공백이 됨
        end_idx += 1
    tmp = reversed(sentence[start_idx:end_idx])
    sentence[start_idx:end_idx] = tmp
    idx = end_idx
    if (
        sentence[end_idx] == " "
    ):  # "<"인 경우에는 +1을 해주면 안되지만 공백인 경우에는 +1을 해줘야 다음 시작 단어로 넘어감
        idx += 1

print("".join(sentence).rstrip())
"""

"""
####### 틀린 경우

import sys
sentence = list(sys.stdin.readline().rstrip())
idx = 0
flag = False

while idx < len(sentence):

    if sentence[idx] == "<":
        flag = True
        idx += 1
    elif sentence[idx] == ">":
        flag = False
        idx += 1
    elif sentence[idx] == " ":
        idx += 1

    if not flag and idx < len(sentence):
        start_idx = idx
        end_idx = idx
        while end_idx < len(sentence) and sentence[end_idx] not in [" ", "<"]:
            end_idx += 1
        tmp = reversed(sentence[start_idx:end_idx])
        sentence[start_idx:end_idx] = tmp
        idx = end_idx
    else:
        idx += 1

print("".join(sentence))

"""
