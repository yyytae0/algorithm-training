def solution(cards1, cards2, goal):
    cnt1, cnt2 = 0, 0
    n1 = len(cards1)
    n2 = len(cards2)
    for i in goal:
        if cnt1 < n1 and i == cards1[cnt1]:
            cnt1 += 1
        elif cnt2 < n2 and i == cards2[cnt2]:
            cnt2 += 1
        else:
            return 'No'
    return 'Yes'
