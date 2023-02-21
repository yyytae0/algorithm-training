def solution(n):
    answer = 0
    prime = [1 for _ in range(1000001)]
    prime[0], prime[1] = 0, 0
    for i in range(2, 1001):
        for j in range(2, 500001):
            if i*j <= 1000000:
                prime[i*j] = 0
            else:
                break
    for i in range(2, n+1):
        if prime[i]:
            answer += 1
    return answer