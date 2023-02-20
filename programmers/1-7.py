def solution(board, moves):
    answer = 0
    length = len(board[0])
    stack = list()
    for idx in moves:
        for i in range(length):
            if board[i][idx-1]:
                if stack:
                    if stack[-1] == board[i][idx-1]:
                        answer += 2
                        board[i][idx - 1] = 0
                        stack.pop()
                        break
                stack.append(board[i][idx-1])
                board[i][idx - 1] = 0
                break

    return answer
