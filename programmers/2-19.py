# def solution(board, skill):
#     answer = 0
#     for lst in skill:
#         if lst[0] == 1:
#             for i in range(lst[1], lst[3] + 1):
#                 for j in range(lst[2], lst[4] + 1):
#                     board[i][j] -= lst[5]
#         else:
#             for i in range(lst[1], lst[3] + 1):
#                 for j in range(lst[2], lst[4] + 1):
#                     board[i][j] += lst[5]
#     for i in board:
#         for j in i:
#             if j > 0:
#                 answer += 1
#     return answer


def solution(board, skill):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            d = board[i][j]
            for lst in skill:
                if lst[0] == 1:
                    if lst[1] <= i <= lst[3] and lst[2] <= j <= lst[4]:
                        d -= lst[5]
                else:
                    if lst[1] <= i <= lst[3] and lst[2] <= j <= lst[4]:
                        d += lst[5]
            if d > 0:
                answer += 1
    return answer
