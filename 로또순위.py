lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# return=[3,5]


def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    change = lottos.count(0)
    a = len([i for i in lottos if i in win_nums])
    return [rank[a+change], rank[a]]


print(solution(lottos, win_nums))
