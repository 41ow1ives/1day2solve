def solution(numbers, target):
    
    numbers = [0] + numbers
    graph = [[] for _ in range(len(numbers))]
    
    for i in range(len(numbers)):
        if i == 0:
            graph[i] += [numbers[i]]
        else:
            for j in graph[i-1]:
                graph[i] += [j+numbers[i], j-numbers[i]]
    return graph[-1].count(target)
