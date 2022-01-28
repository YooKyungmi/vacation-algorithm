id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
# result=[2,1,1,0]


def solution(id_list, report, k):
    data = {}
    repData = []
    for i in id_list:
        data[i] = [0, []]

    report = set(report)
    for j in report:
        j = j.split()
        data[j[1]][1].append(j[0])
        if len(data[j[1]][1]) >= k:
            repData.append(j[1])

    repData = list(map(lambda x: data[x][1] if len(
        data[x][1]) >= k else [], id_list))
    repData = sum(repData, [])
    print(repData)

    answer = list(map(lambda x: repData.count(x), id_list))
    return answer


print(solution(id_list, report, k))
