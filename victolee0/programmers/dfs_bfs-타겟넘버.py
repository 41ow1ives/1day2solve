from itertools import product

def solution(numbers, target):
    t = [[-1, 1]] * len(numbers)
    m = list(product(*t))
    answer = 0
    for num in m:
        tmp = 0
        for i, j in zip(num, numbers):
            tmp = tmp + i * j
        if tmp == target:
            answer += 1
    return answer