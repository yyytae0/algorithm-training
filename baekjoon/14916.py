n = int(input())

if n == 1 or n == 3:
    ans = -1
elif n % 5 == 0:
    ans = n//5
elif n % 5 == 1:
    ans = n//5 - 1 + 3
elif n % 5 == 2:
    ans = n//5 + 1
elif n % 5 == 3:
    ans = n//5 - 1 + 4
elif n % 5 == 4:
    ans = n//5 + 2

print(ans)
