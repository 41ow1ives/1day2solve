# https://www.acmicpc.net/problem/1935
# 후위 표기식2 (SILVER III)

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
postfix_notation = sys.stdin.readline().rstrip()

operand = defaultdict()
stack = []

for word in postfix_notation:
    if word not in operand.keys() and word.isalpha():  # 피연산자인데 값이 지정 안되었을 때
        operand[word] = int(sys.stdin.readline())
        stack.append(operand[word])
    elif word in operand.keys():  # 피연산자이며 값이 이미 지정되었을 때
        stack.append(operand[word])
    else:  # word is an operator 연산자일 때
        second = stack.pop()
        first = stack.pop()
        tmp = eval(f"{first}{word}{second}")  # 가장 뒤에 있는게 Second고 그 앞에가 first인거 유의
        stack.append(tmp)
print(f"{stack[0]:.2f}")


"""
###### 후위표기식이 뭔지 몰라서 완전 잘못 풀었음

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
postfix_notation = sys.stdin.readline().rstrip()
operand_dict, operand_list = defaultdict(), []  # 피연산자
operator = []  # 연산자

for word in postfix_notation:
    # 후위표기식의 글자 하나씩을 돌면서 값을 저장한다.
    if (
        word not in operand_dict.keys() and word.isalpha()
    ):  # 피연산자이면서 아직 값을 입력 받지 않은 경우 입력 받음
        operand_dict[word] = int(sys.stdin.readline())
        operand_list.append(word)
    elif not word.isalpha():  # 연산자인 경우, 연산자 리스트에 넣어줌
        operator.append(word)
    else:  # word in operand_dict.keys()
        operand_list.append(word)
answer = [operand_dict[operand_list[0]]]
for idx, o in enumerate(operator):
    front = answer[-1]
    back = operand_dict[operand_list[idx + 1]]
    print(f"{front}{o}{back}")
    tmp = eval(f"{front}{o}{back}")
    answer.append(tmp)
    print(answer)

print(f"{answer.pop() : .2f}")
"""
