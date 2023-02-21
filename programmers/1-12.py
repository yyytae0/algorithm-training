def solution(s, skip, index):
    answer = ''
    lst = []
    for i in range(97, 123):
        lst.append(chr(i))
    for i in skip:
        lst.remove(i)
    n = len(lst)
    for i in s:
        for j in range(n):
            if lst[j] == i:
                nj = j + index
                while nj >= n:
                    nj -= n
                answer += lst[nj]
                break
    return answer
