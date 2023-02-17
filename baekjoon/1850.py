def gcd(a, b):
    if b > a:
        a, b = b, a
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b


a, b = map(int, input().split())
ans = gcd(a, b)
print('1'*ans)
