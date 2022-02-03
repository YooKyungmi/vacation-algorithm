import re
new_id = "...!@BaT#*..y.abcdefghijklm"


def solution(new_id):
    answer = new_id.lower()  # 1단계
    answer = re.sub("[^a-z0-9-_.]", "", answer)  # 2단계
    answer = re.sub('[.]+', '.', answer)  # 3단계
    answer = re.sub('^[.]|[].]$', '', answer)  # 4단계
    if len(answer) == 0:
        answer = 'a'  # 5단계
    if len(answer) >= 16:  # 6단계
        answer = answer[:15]
        answer = re.sub('^[.]|[.]$', '', answer)
    ans = answer[-1]
    while(len(answer) <= 2):
        answer += ans  # 7단계

    return answer


print(solution(new_id))
