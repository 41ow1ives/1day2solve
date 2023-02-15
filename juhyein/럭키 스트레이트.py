N = input()
l = len(N)
left = [int(N[i]) for i in range(l//2)]
right = [int(N[i]) for i in range(l//2,l)]


if sum(left) == sum(right):print("LUCKY")
else:print("READY")
