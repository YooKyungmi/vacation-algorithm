places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#result= [1, 0, 1, 1, 1]


def solution(places):
    a = places[1]
    indexList = []
    for j in range(5):
        indexList.append([i for i, char in enumerate(a[j]) if char == 'P'])
    print(indexList)
    answer = []
    return answer


print(solution(places))
