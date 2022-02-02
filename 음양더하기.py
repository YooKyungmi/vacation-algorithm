absolutes = [4, 7, 12]
signs = [True, False, True]


def solution(absolutes, signs):

    answer = list(
        map(lambda x, y: x if y == True else -x, absolutes, signs))
    answer = sum(answer)
    return answer


print(solution(absolutes, signs))
