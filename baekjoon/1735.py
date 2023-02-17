def gcd(a, b):
    if b > a:
        a, b = b, a
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b


a, b = map(int, input().split())
c, d = map(int, input().split())

x = a*d + b*c
y = b*d
d = gcd(x, y)
print(x//d, y//d)
