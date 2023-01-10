from collections import deque    

def solution(rc, operations):
    r = len(rc)
    c = len(rc[0])
    left = deque([rc[i][0] for i in range(r)])
    right = deque([rc[i][c-1] for i in range(r)])
    rows = deque([deque(rc[i][1:c-1]) for i in range(r)])
    
    for op in operations:
        if op == "ShiftRow":
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            rows.appendleft(rows.pop())
        else:
            rows[0].appendleft(left.popleft())
            right.appendleft(rows[0].pop())
            rows[r-1].append(right.pop())
            left.append(rows[r-1].popleft())

    result = []
    for i in range(r):
        result.append([left[i]] + list(rows[i]) + [right[i]])


    return result