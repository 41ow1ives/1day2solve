def solution(brown, yellow):
    nm = brown + yellow
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == yellow:
            return sorted([n, m], reverse = True)
