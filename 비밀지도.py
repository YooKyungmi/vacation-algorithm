import re
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
# 출력	["#####","# # #", "### #", "# ##", "#####"]


def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        a = format((arr1[i] | arr2[i]), 'b')
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        if len(a) < n:
            a = ' '+a
        answer.append(a)

    return answer


print(solution(n, arr1, arr2))
