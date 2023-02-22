def solution(storey:int)->int:
    """
    storey가 n자리 숫자이고 n번째자리수의 값이 5 이하라면 10^(n-1)의 배수, 6 이상이라면 10^(n)의 배수로 만들어 주어야 최소로 계산할 수 있음
    이때 i번째 자리 값이 5 이하라면 빼주는 것이, 6 이상이라면 더해주는 것이 이득
    단, i+1번째 자리 값이 5 이상이라면 5 이상인 i번째 자리 값을 더해주는 것이 이득
    """
    answer = 0
    idx = 1
    while idx <= len(str(storey)):
        number = storey%10**(idx)
        number = number//10**(idx-1)
        storey = storey - number * 10**(idx-1)
        if number <= 4 :
            answer += number
        elif number >= 6 :
            answer += 10 - number
            storey = storey + 10**(idx)
        else: # number == 5
            answer += number # 마지막 자릿수라면 그냥 더해주고 끝냄
            if idx <= len(str(storey)): # 마지막 자릿수가 아니라면
                next_number = storey%10**(idx+1) # 다음 자릿수 체크
                next_number = next_number//10**(idx)
                if next_number >= 5: # 다음 자리 수가 5 이상이라면
                    storey =  storey + 10**(idx)
        idx+=1
    return answer


########## 틀린 코드
# 이번자리 숫자가 5일 때 다음자리 숫자가 5 이상이라면 빼주는게 아니라 더해주어야함을 놓침
"""
def solution(storey):
    # storey가 n자리면 10^(n-1)의 배수로 만들어 주어야 최소로 계산할 수 있음
    # 이때 i번째 자리 값이 5 이하라면 빼주는 것이, 6 이상이라면 더해주는 것이 이득
    
    answer = 0
    storey = str(storey)[::-1] # 1의 자리부터 체크해주어야하므로 reverse 해준다.
    idx = 0
    flag = False
    while idx < len(storey): # storey가 업데이트 되어야하므로 while문 이용
        number = storey[idx]
        if int(number) <= 5: # 5 이하면 빼준다
            answer += int(number)
            storey = storey[:idx] + '0' + storey[idx+1:]
        elif int(number) > 5: # 6 이상이면 더해준다
            answer += 10 - int(number)
            
            if idx+1!=len(storey): # number가 가장 마지막자리 수가 아니라면
                next_number = int(storey[idx+1])+1
                if next_number == 10:
                    storey = storey[:idx] + '0' + storey[idx+1:]
                    jdx = 1
                    while (idx+jdx<len(storey)) and (int(storey[idx+jdx])+1 == 10):
                        storey = storey[:idx+jdx] + '0' + storey[idx+jdx+1:]
                        jdx += 1
                    if storey[idx+jdx-1] == '0':
                        storey = storey + '1'
                else: # 1 넘겨준 다음자리 수가 9 이하라면
                    storey = storey[:idx] + '0' + str(int(storey[idx+1])+1) + storey[idx+2:]
            else: # number가 가장 마지막자리 수라면 자릿수가 하나 올라가니까 +1 해줌
                answer += 1
        idx += 1
    return answer
"""