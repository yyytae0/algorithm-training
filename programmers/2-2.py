def solution(book_time):
    cnt = [0 for _ in range(1441)]
    for i in book_time:
        s = int(i[0][:2]) * 60 + int(i[0][-2:])
        g = int(i[1][:2]) * 60 + int(i[1][-2:]) + 9
        if g > 1439:
            g = 1439
        for j in range(s, g+1):
            cnt[j] += 1
    answer = max(cnt)
    return answer