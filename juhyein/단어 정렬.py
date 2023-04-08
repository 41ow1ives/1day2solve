N = int(input())
words = []
for _ in range(N):
    w = input()
    words.append(w)
    
words = list(set(words))

words = sorted(words, key = lambda x : (len(x), x))

for w in words:
    print(w)
