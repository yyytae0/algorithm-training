n = int(input())
lst = list(int(input()) for _ in range(n))
lst.sort()
mx = 0
cnt = n
for i in range(n):
    now = lst[i] * cnt
    if now > mx:
        mx = now
    cnt -= 1
print(mx)
