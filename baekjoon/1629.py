def check(x, y):
    if y == 1:
        return x
    else:
        small = check(x, y//2)
        if y % 2 == 0:
            return ((small % c) * (small % c)) % c
        else:
            return ((small % c) * (small % c) * x) % c


a, b, c = map(int, input().split())
ans = check(a, b)
print(ans % c)
