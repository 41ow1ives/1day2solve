# 프로그래머스 Summer/Winter Coding(~2018)
# Lv 2

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:

        i = 0
        possible = True
        for s in skill_tree:
            if s in skill:
                if s == skill[i]:
                    i += 1
                else:
                    possible = False
                    break

        if possible:
            answer += 1

    return answer