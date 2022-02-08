board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    result = []
    answer = 0
    for j in moves:
        for i in range(len(board)-1, 0, -1):
            if board[i-1][j-1] == 0:
                if board[i][j-1] != 0:
                    result.append(board[i][j-1])
                    board[i][j-1] = 0
                break
        if len(result) >= 2 and result[-1] == result[-2]:
            del result[-2:]
            answer += 2
    return answer


print(solution(board, moves))
