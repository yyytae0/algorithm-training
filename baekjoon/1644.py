def check():
    ans = 0
    for i in range(N):
        idx = i
        sm = 0
        while True:
            sm = sm + lst[idx]
            idx += 1
            if sm == n:
                ans += 1
                break
            if sm > n or idx == N:
                break
    return ans


n = int(input())
prime = [1 for _ in range(n+1)]
N = 0
lst = list()
for i in range(2, n+1):
    if i < int(n**(1/2)+1):
        if prime[i]:
            N += 1
            lst.append(i)
            for j in range(2, n // 2 + 1):
                if i*j > n:
                    break
                prime[i * j] = 0
    else:
        if prime[i]:
            N += 1
            lst.append(i)

print(check())
