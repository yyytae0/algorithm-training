n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dummy = 300000
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i]+lst[j]+lst[k] > m:
                break

            if m - (lst[i]+lst[j]+lst[k]) < dummy:
                dummy = m - (lst[i]+lst[j]+lst[k])

            if dummy == 0:
                break
        if dummy == 0:
            break
    if dummy == 0:
        break

print(m-dummy)
