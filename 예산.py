#d = [1, 3, 2, 5, 4]
d = [2, 2, 3, 3]
budget = 10


def solution(d, budget):
    d.sort()
    sum = 0
    for i in range(len(d)):
        if sum+d[i] <= budget:
            answer = i+1
        else:
            break
    return answer


print(solution(d, budget))
