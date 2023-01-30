from sys import stdin

prime = [True] * 10001
prime[0] = False
prime[1] = False
prime_lst = list()
for i in range(10001):
    if prime[i]:
        prime_lst.append(i)
        for j in range(2*i, 10001, i):
            prime[j] = False

ip = int(input())

for i in range(ip):
    ans = list()
    n = int(stdin.readline())
    dummy = 10000
    for j in prime_lst:
        if j > n or j > n-j:
            break

        if prime[n-j]:
            ans.append([j, n - j])

    print(*ans[-1])
