n = input()
a = len(n)
ans = a * (int(n) - 10**(a-1) + 1)
a = a-1
while a > 0:
    ans += a * (10**a - 10**(a-1))
    a -= 1
print(ans)
