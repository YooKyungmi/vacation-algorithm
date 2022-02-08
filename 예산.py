#d = [1, 3, 2, 5, 4]
d = [2, 2, 3, 3]
budget = 10


def solution(d, budget):
    d.sort()
    for i in range(1, len(d)+1):
        if sum(d[:i]) <= budget:
            answer = i
        else:
            break
    return answer


print(solution(d, budget))
