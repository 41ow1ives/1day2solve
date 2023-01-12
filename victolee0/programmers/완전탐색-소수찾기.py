import math
from itertools import permutations

def is_prime(num):
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True
        

def solution(numbers):
    num = set()
    for i in range(1, len(numbers)+1):
        tmp = list(permutations(numbers, i))
        for n in tmp:
            num.add(int(''.join(n)))
    answer = 0
    for i in num:
        if i < 2:
            continue
        if is_prime(i):
            answer += 1
    
    return answer