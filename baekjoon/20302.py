prime = [[1] for _ in range(100000)]
count = [0 for _ in range(100000)]
prime[1] = []
n = int(input())
lst = list(input().split())
prime_lst = []


def pos(a):
    if a > 0:
        return a
    return -a


def solve():
    now = int(lst[0])
    now = pos(now)
    t = now
    for i in prime[t]:
        if i == 0:
            continue
        if i == 1:
            count[t] += 1
            break
        while now % i == 0:
            now = now // i
            count[i] += 1

    if n > 1:
        for i in range(n - 1):
            now = int(lst[2 * i + 2])
            now = pos(now)
            t = now
            if lst[2 * i + 1] == '*':
                for j in prime[t]:
                    if j == 0:
                        continue
                    if j == 1:
                        count[t] += 1
                        break
                    while now % j == 0:
                        now = now // j
                        count[j] += 1

            else:
                for j in prime[t]:
                    if j == 0:
                        continue
                    if j == 1:
                        count[t] -= 1
                        break
                    while now % j == 0:
                        now = now // j
                        count[j] -= 1

    for i in prime_lst:
        if count[i] < 0:
            print("toothpaste")
            return
    print("mint chocolate")
    return


for i in range(2, 100000):
    if prime[i][0]:
        prime_lst.append(i)
        for j in range(2, 50000):
            if i*j >= 100000:
                break
            prime[i*j].append(i)
            prime[i*j][0] = 0

solve()
