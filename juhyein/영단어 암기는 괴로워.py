N, M = map(int , input().split())
words = []
for _ in range(N):
    x = input()
    if len(x)>=M:
        words.append(x)
        
from collections import Counter 
cnt = Counter(words)

words = sorted(words, key = lambda x :(-int(cnt[x]), len(x), x))
for w in set(words):
    print(w)
