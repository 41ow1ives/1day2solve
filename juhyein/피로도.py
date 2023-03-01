import itertools
def solution(k, dungeons):
    answer = -1
    visited = 0
    for dungeon_permutations in itertools.permutations(dungeons):
        have, count = k, 0
        for need, cost in dungeon_permutations:
            if have >= need and have >= cost:
                have -= cost
                count += 1
        visited = max(visited, count)
    answer = visited
    return answer
