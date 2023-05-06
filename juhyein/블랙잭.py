n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_val = 0
def blackjack(index=0, visit_index=-1, arr=[], length=n, key=m):
    if index == 3:
        if sum(arr) > key: return
        global max_val
        if max_val < sum(arr):
            max_val = sum(arr)
            return
    else:
        for i in range(visit_index + 1, length):
            blackjack(index=index+1, visit_index=i, arr= arr+[cards[i]])


blackjack()
print(max_val)
