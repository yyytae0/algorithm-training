def solution(arr):
    answer = 1
    d = [1 for _ in range(101)]
    d[0] = 0
    d[1] = 0
    prime = {}
    for i in range(51):
        if d[i]:
            prime[i] = 0
            for j in range(2, 51):
                if i*j > 100:
                    break
                d[i*j] = 0
    for i in arr:
        dummy = i
        for j in prime:
            cnt = 0
            while not (dummy % j):
                dummy = dummy // j
                cnt += 1
            prime[j] = max(prime[j], cnt)

    for i in prime:
        if prime[i]:
            answer = answer * (i**prime[i])
    return answer