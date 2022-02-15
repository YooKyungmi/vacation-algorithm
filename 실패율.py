stages = [3, 3, 3, 3, 3, 3, 3]
N = 5


def solution(N, stages):
    user = [0]*(N+1)
    for i in stages:
        user[i-1] += 1
    fail = list(
        map(lambda x: user[x]/sum(user[x:]) if user[x] != 0 else 0, range(N)))
    answer = dict(zip(range(1, N+1), fail))
    answer = sorted(answer, key=answer.get, reverse=True)
    return answer


print(solution(N, stages))
