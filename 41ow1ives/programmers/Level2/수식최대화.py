# https://school.programmers.co.kr/learn/courses/30/lessons/67257
# 수식최대화 (Lv.2)

# expression의 길이가 100 이하이며 연산자의 종류 또한 최대 3개이므로 3!의 경우의수가 존재함 -> 완전탐색

from itertools import permutations


def solution(expression):

    # 일단 연산자와 숫자 분리
    ope_list, ope_idx = [], 0
    number_list = []
    for idx, exp in enumerate(expression):
        if exp in ["+", "-", "*"]:  # 연산자라면
            ope_list.append(exp)  # 연산자 리스트에 연산자 더해주고
            number_list.append(
                int(expression[ope_idx:idx])
            )  # 그 앞을 이루는 숫자를 숫자 리스트에 더해준다
            ope_idx = idx + 1
    number_list.append(int(expression[ope_idx:]))  # 마지막 숫자는 뒤에 연산자 없어서 따로 넣어준다

    # 연산자 set으로 permutation
    ope_p = list(permutations(set(ope_list)))

    answer = 0
    for permutation in ope_p:
        # 각 permutation 조합의 결과를 체크할 때 마다 원본을 불러온다.
        tmp_number_list = number_list[1:]
        tmp_ope_list = ope_list[:]

        # permutation 안의 operator를 돈 결과를 저장할 리스트.
        stack = [number_list[0]]
        cur_ope_list = []

        # priority대로 체크한다.
        for ope in permutation:
            for check_ope, check_num in zip(tmp_ope_list, tmp_number_list):
                stack.append(check_num)
                if check_ope == ope:
                    second = stack.pop()
                    first = stack.pop()
                    tmp = eval(f"{first}{ope}{second}")
                    stack.append(tmp)
                else:
                    cur_ope_list.append(check_ope)

            tmp_ope_list = cur_ope_list[:]
            cur_ope_list = []

            tmp_number_list = stack[1:]
            stack = [stack[0]]

        answer = max(abs(stack[0]), answer)

    return answer


"""
# 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하기
# 이때 2개 이상의 연산자가 동일한 순위를 가질 수는 없음
# 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출한다

# 연산자의 최대 개수는 3가지이므로 최대 3! + expression 최대길이 100 => for문 돌려도 됨

from itertools import permutations
import re

def solution(expression: str):
    
    # expression 안에 어떤 연산자가 존재하는지 파악하기
    operator_list = [ exp for exp in expression if not exp.isdigit()]
    operator_per = list(set(operator_list))
    operator_per = list(permutations(operator_per)) # 연산자들의 Permutation 구하기
    
    # expression 안의 숫자들만 구하기
    number_list = re.split('[*\-+]', expression)
    
    # permutation 경우의 수 돌면서 값 저장하기
    answer = []
    for ope in operator_per:
        tmp_expression = expression
        for p in ope:
            if p != "-": 
                while tmp_expression.find(p) != -1:
                    if p == "+":
                        cur_match = re.search(r"\d+\+\d+", tmp_expression)
                    elif p == "*":
                        cur_match = re.search(r"\d+\*\d+", tmp_expression)
                    try:
                        cur_eval = eval(cur_match.group())
                        tmp_expression = tmp_expression[:cur_match.span()[0]] + str(cur_eval) + tmp_expression[cur_match.span()[1]:]
                    except:
                        print(tmp_expression)
            else: # p=="-"
                while re.findall(r"\d+\-\d+", tmp_expression) != []:
                    cur_match = re.search(r"\d+\-\d+", tmp_expression)
                    try:
                        cur_eval = eval(cur_match.group())
                        tmp_expression = tmp_expression[:cur_match.span()[0]] + str(cur_eval) + tmp_expression[cur_match.span()[1]:]
                    except:
                        print(tmp_expression)
                
            answer.append(tmp_expression)
    return answer

"""
