answer = 10**8


def check(cnt, dummy, lst, s):
    global answer
    if cnt == 0:
        dummy = min(dummy + s[cnt] + lst[cnt], dummy + 10 - s[cnt] - lst[cnt] + 1)
        lst[cnt] = 0
        if dummy < answer:
            answer = dummy
        return

    now = [s[cnt] + lst[cnt], 10 - s[cnt] - lst[cnt]]
    for i in range(2):
        lst[cnt-1] += i
        check(cnt-1, dummy + now[i], lst, s)
        lst[cnt-1] = 0


def solution(storey):
    global answer
    s = list(map(int, str(storey)))
    n = len(s)
    lst = [0 for _ in range(n + 1)]
    answer = 10 ** 8
    check(n-1, 0, lst, s)
    return answer


print(solution(999))
print(solution(678))
