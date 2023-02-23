# https://www.acmicpc.net/problem/4344
# 평균은 넘겠지

"""
asterisk로 리스트 한번에 받기
f-string으로 소수점 formatting
"""
test_num = int(input())

for _ in range(test_num):
    student_num, *scores = map(int, input().split())
    avg = sum(scores) // student_num
    avg_or_not = [1 if score > avg else 0 for score in scores]
    print(f"{(sum(avg_or_not) / student_num) * 100:.3f}%")
