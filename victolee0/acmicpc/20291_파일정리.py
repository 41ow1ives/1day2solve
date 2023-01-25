import sys

n = int(sys.stdin.readline().strip())

dic = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    tmp = name.split('.')[1]
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

key = list(sorted(dic.keys()))
for k in key:
    print(f'{k} {dic[k]}')