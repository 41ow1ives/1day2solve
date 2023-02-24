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
