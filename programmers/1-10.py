def solution(answers):
    answer = []
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lst3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [[1, 0], [2, 0], [3, 0]]
    for idx, i in enumerate(answers):
        if i == lst1[idx % 5]:
            cnt[0][1] += 1
        if i == lst2[idx % 8]:
            cnt[1][1] += 1
        if i == lst3[idx % 10]:
            cnt[2][1] += 1
    cnt.sort(key=lambda x: (-x[1], x[0]))
    mx = cnt[0][1]
    for i in range(3):
        if cnt[i][1] >= mx:
            answer.append(cnt[i][0])

    return answer
