# 프로그래머스 2022 카카오 테크 인턴십
# Lv 2

from collections import deque
def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    cnt = 0

    for _ in range(2 * (len(q1) + len(q2))):

        if s1 > s2:
            k = q1.popleft()
            q2.append(k)
            s1 -= k
            s2 += k
            cnt += 1

        elif s1 < s2:
            k = q2.popleft()
            q1.append(k)
            s2 -= k
            s1 += k
            cnt += 1

        else:
            return cnt

    return -1