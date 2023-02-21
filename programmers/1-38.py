def solution(n, arr1, arr2):
    answer = []
    lst = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dummy = ''
        n1 = arr1[i]
        nj = 1
        while n1:
            lst[i][-nj] += n1 % 2
            n1 = n1//2
            nj += 1
        m1 = arr2[i]
        mj = 1
        while m1:
            lst[i][-mj] += m1 % 2
            m1 = m1 // 2
            mj += 1
        for j in lst[i]:
            if j:
                dummy += '#'
            else:
                dummy += ' '
        answer.append(dummy)
    return answer