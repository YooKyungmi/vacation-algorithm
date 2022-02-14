import itertools

nums = [1, 2, 7, 6, 4]
# return 4


def solution(nums):
    c = [sum(i) for i in itertools.combinations(nums, 3)]
    ans = []
    for i in c:
        for j in range(2, i):
            if i % 2 != 0 and i % 3 != 0:
                if i % j == 0:
                    break
                if j == (i-1):
                    ans.append(i)
    return len(ans)


print(solution(nums))
