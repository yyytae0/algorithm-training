def solution(lottos, win_nums):
    answer = []
    cnt0, cnt1 = 0, 0
    for i in lottos:
        if i == 0:
            cnt0 += 1
        else:
            if i in win_nums:
                cnt1 += 1
    a, b = 6 - cnt0 - cnt1 + 1, 6 - cnt1 + 1
    if a > 6:
        a = 6
    if b > 6:
        b = 6
    answer = [a, b]
    return answer
