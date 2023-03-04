# https://www.acmicpc.net/problem/12789
# 도키도키 간식드리미 (SILVER III)

import sys

n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().rstrip().split()))
tmp_line = [9999]  # 20번에서 indexing 편하게 하려고
cur = 1
flag = True

for student in students:

    if cur == student:  # 자기 차례인 학생이라면 tmp_line에 넣지 않는다
        cur += 1  # 다음 차례로 넘겨주고 tmp_line에 쌓여 있는 애들을 빼준다
        while cur == tmp_line[-1]:  # tmp_line의 맨 위에 있는 친구가 다음 차례라면
            tmp_line.pop()  # tmp_line에서 빼주고
            cur += 1  # 다음 차례로 넘겨준다.

    else:
        if tmp_line[-1] > student:
            tmp_line.append(student)
        else:  # tmp_line의 맨 앞에 있는 친구보다 이번에 들어갈 친구의 차례가 크다면
            print("Sad")
            flag = False
            break  # for문은 끝나도 밑에 print("Nice")를 거치므로 break

if flag == True:
    print("Nice")
