# 제목 : 부등호
# 분류 : 완전탐색/백트래킹, Silver 2
# 출처 : 백준 2529

n = int(input())
ineq_lst = ['<'] + list(input().split())
ans = []
visited = [False] * 10


def find(idx, seq):
    global ans
    if idx == n+1:
        ans.append(''.join(map(str, seq[1:])))
        return

    ineq = ineq_lst[idx]
    if ineq == '<':
        for i in [k for k in range(10) if seq[-1] < k]:
            if visited[i]: continue
            seq.append(i)
            visited[i] = True
            find(idx + 1, seq)
            visited[i] = False
            seq.pop()

    else:
        for i in [k for k in range(10) if seq[-1] > k]:
            if visited[i]: continue
            seq.append(i)
            visited[i] = True
            find(idx + 1, seq)
            visited[i] = False
            seq.pop()


find(0, [-1])
print(max(ans))
print(min(ans))



'''
조금 더 빠른 방법
0부터 9까지 차례대로 탐색을 하기 때문에, 
항상 처음에 구해지는 수가 최소, 마지막에 구해지는 수가 최대가 됨
'''
n = int(input())
ineq_lst = list(input().split())
min_ans, max_ans = "", ""
visited = [False] * 10

def check(a, b, ineq):
    if ineq == '<':
        return a < b
    else:
        return a > b
    return True

def find(idx, s):
    global min_ans, max_ans

    if idx == n+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if visited[i]: continue
        if idx == 0 or check(int(s[-1]), i, ineq_lst[idx-1]):
            visited[i] = True
            find(idx + 1, s + str(i))
            visited[i] = False

find(0, "")
print(max_ans)
print(min_ans)