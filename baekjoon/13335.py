n, w, L = map(int, input().split())
lst = list(map(int, input().split()))
d = [0 for _ in range(n)]
total = 0
t = 0
for i in range(n):
    total += lst[i]
    if total <= L:
        t += 1
        for j in range(i):
            if d[j] < w+1:
                d[j] += 1
                if d[j] == w+1:
                    total -= lst[j]
    while total > L:
        t += 1
        for j in range(i):
            if d[j] < w+1:
                d[j] += 1
                if d[j] == w+1:
                    total -= lst[j]
    d[i] += 1
while d[n-1] < w+1:
    t += 1
    d[n-1] += 1
print(t)
