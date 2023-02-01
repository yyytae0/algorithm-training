n, m = map(int, input().split())
lst = list(map(int, input().split()))
counter = [0 for _ in range(m)]
counter[lst[0] % m] += 1

for i in range(1, n):
    lst[i] = lst[i] + lst[i-1]
    counter[lst[i] % m] += 1

ans = counter[0]
for i in counter:
    ans += i*(i-1)//2

print(ans)
