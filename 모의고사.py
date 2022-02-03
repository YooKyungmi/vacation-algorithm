#answers = [1, 3, 2, 4, 2]
answers = [3, 3, 2, 1, 5]


def solution(answers):
    stu = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5],
           3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    score = {1: 0, 2: 0, 3: 0}
    answer = []

    for i in range(1, 4):
        score[i] = sum(1 if stu == ans else 0 for stu,
                       ans in zip(stu[i], answers))

    score = sorted(score.items(), key=lambda x: x[1], reverse=True)

    for i in score:
        if i[1] == score[0][1]:
            answer.append(i[0])

    return answer


print(solution(answers))
