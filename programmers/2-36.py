def change(n, k):
    d = n
    c = ''
    while d:
        c = str(d % k) + c
        d = d//k
    return c


def solution(n, k):
    s = change(n, k)
    lst = [int(i) for i in list(s.split('0')) if i != '']
    answer = 0
    print(lst)
    for i in lst:
        for j in range(2, int(i**(1/2))+1):
            if not i % j:
                break
        else:
            if i >= 2:
                answer += 1
    return answer