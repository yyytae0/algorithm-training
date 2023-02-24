def postorder(a):
    global ans
    dummy = []
    for i in dct[a]:
        postorder(i[0])
        dummy.append(lst[i[0]] + i[1])
    if dummy:
        lst[a] = max(dummy)
        for i in range(len(dummy)):
            for j in range(i + 1, len(dummy)):
                if dummy[i] + dummy[j] > ans:
                    ans = dummy[i] + dummy[j]
        if lst[a] > ans:
            ans = lst[a]
    else:
        lst[a] = 0


n = int(input())
dct = dict()
for i in range(n):
    d = list(map(int, input().split()))
    dct[d[0]] = []
    for j in range(1, 10, 2):
        if d[j] == -1:
            break
        else:
            dct[d[0]].append([d[j], d[j+1]])
lst = [0 for _ in range(n+1)]
ans = 0
postorder(1)
print(ans)