# isdigit()
s = "234"
# 234567


def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']
    for i in range(9):
        if num[i] in s:
            s = s.replace(num[i], str(i))
    return int(s)


print(solution(s))
