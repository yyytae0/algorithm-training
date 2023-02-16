def gcd(a, b):
    while True:
        if a > b:
            if a % b == 0:
                return b
            a = a % b
        else:
            if b % a == 0:
                return a
            b = b % a


ip = int(input())

for case in range(1, ip+1):
    lst = list(map(int, input().split()))
    n = lst[0]
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ans += gcd(lst[i], lst[j])
    print(ans)
