# https://www.acmicpc.net/problem/9012
# 괄호

"""
list에 값을 받아서 걔를 확인하기 보다는 숫자로 경우를 나누어 체크하기

import sys

T = int(sys.stdin.readline())
def vps():
    k = 0
    s = list(sys.stdin.readline().strip())

    for _ in range(len(s)):
        j = s.pop()
        if j == ')':
            k += 1
        elif j == '(':
            k -= 1
        if k == -1:
            return 'NO' # 이 경우를 따로 안 빼주면 )()( 가 통과됨
    if k == 0:
        return 'YES'
    else:
        return 'NO'
    
for i in range(T):
    print(vps())
    
"""
import sys

num = int(sys.stdin.readline())

for _ in range(num):
    ps = ["*"]
    letters = sys.stdin.readline()
    for letter in letters:
        if letter == ")":
            if ps[-1] == "(":
                ps.pop()
            else:
                ps.append(letter)
        elif letter == "(":
            ps.append(letter)
    if len(ps) != 1:
        print("NO")
    else:
        print("YES")
