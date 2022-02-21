s = "try hello world"


def solution(s):
    answer = []
    for i in s.split(" "):
        ans = list(map(lambda x, y: x.upper() if y %
                   2 == 0 else x.lower(), i, range(len(i))))
        answer.append("".join(ans))
    return " ".join(answer)


print(solution(s))
