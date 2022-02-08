#d = [1, 3, 2, 5, 4]
d = [2, 2, 3, 3]
budget = 10


def solution(d, budget):
    d.sort()
    if sum(d[:len(d)//2]) >= budget:
        for i in range(1, len(d)//2):
            if sum(d[:i]) <= budget:
                answer = i
            else:
                break
    else:
        for i in range(len(d)//2, len(d)+1):
            if sum(d[:i]) <= budget:
                answer = i
            else:
                break
    return answer


print(solution(d, budget))
