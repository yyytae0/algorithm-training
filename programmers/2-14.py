def solution(board):
    cnt_o = 0
    cnt_x = 0
    for i in board:
        for j in i:
            if j == 'O':
                cnt_o += 1
            elif j == 'X':
                cnt_x += 1
    if (cnt_o - cnt_x) != 1 and (cnt_o - cnt_x) != 0:
        return 0
    cnt1 = 0
    cnt2 = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'O':
                break
        else:
            cnt1 += 1
        for j in range(3):
            if board[i][j] != 'X':
                break
        else:
            cnt2 += 1
        for j in range(3):
            if board[j][i] != 'O':
                break
        else:
            cnt1 += 1
        for j in range(3):
            if board[j][i] != 'X':
                break
        else:
            cnt2 += 1
        if cnt1 and cnt2:
            return 0
    for i in range(3):
        if board[i][i] != 'O':
            break
    else:
        cnt1 += 1
    for i in range(3):
        if board[i][i] != 'X':
            break
    else:
        cnt2 += 1
    for i in range(3):
        if board[i][2-i] != 'O':
            break
    else:
        cnt1 += 1
    for i in range(3):
        if board[i][2-i] != 'X':
            break
    else:
        cnt2 += 1
    if cnt1:
        if cnt_o - cnt_x != 1:
            return 0
    if cnt2:
        if cnt_o - cnt_x != 0:
            return 0
    return 1
