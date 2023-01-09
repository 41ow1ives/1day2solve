n = int(input())

cols = [0 for _ in range(n)]
answer = 0

def attackable(x1, y1, x2, y2):
    if y1 == y2:
        return True
    if x1 - y1 == x2 - y2:
        return True
    if x1 + y1 == x2 + y2:
        return True
    return False

def rec_func(row):

    if row == n:
        global answer
        answer += 1
    else:
        for cand in range(n):
            possible = True
            for i in range(row):
                if attackable(i, cols[i], row, cand):
                    possible = False
                    break
            if possible:
                cols[row] = cand
                rec_func(row + 1)
                cols[row] = 0
                

rec_func(0)
print(answer)