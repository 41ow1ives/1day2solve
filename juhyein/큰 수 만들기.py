# 그리디
# 어떤 숫자에서 K개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자

# 내 답안 (테스트케이스 3번 오류)
def solution(number, k):
    number = list(str(number))
    answer = ''
    rm = sorted(number)
    
    for i in range(k):
        number.remove(rm[i])    
    
    return ''.join(number)


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
