def calc_brown(w, h):
    return (w + h) * 2 - 4

def calc_yellow(w, h, brown):
    return w * h - brown



def solution(brown, yellow):
    wh = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            wh += [(i, yellow//i)]
    
    for w, h in wh:
        if (w + 2 + h + 2) * 2 - 4 == brown:
            answer = [w + 2, h + 2]
    answer = sorted(answer, reverse = True)
    return answer