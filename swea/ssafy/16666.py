def mini():
    dummy = n[:]
    if n[0] == mn:
        for num in range(10):
            for i in range(l-1, 0, -1):
                if n[i] == num:
                    old = i
                    break
            else:
                continue
            for i in range(1, old):
                if n[i] > num:
                    dummy[i], dummy[old] = dummy[old], dummy[i]
                    break
            else:
                continue
            break
    else:
        for i in range(l-1, 0, -1):
            if n[i] == mn:
                dummy[i], dummy[0] = dummy[0], dummy[i]
                break
    d = ''
    for k in dummy:
        d += str(k)
    return d


def maxi():
    dummy = n[:]
    now = -1
    for i in range(l):
        if n[i] == srt[now]:
            now -= 1
            continue
        else:
            for j in range(i + 1, l):
                if n[j] == srt[now]:
                    idx = j
            dummy[idx], dummy[i] = dummy[i], dummy[idx]
            break
    d = ''
    for k in dummy:
        d += str(k)
    return d


ip = int(input())

for case in range(1, ip+1):
    n = list(map(int, input()))
    mx = max(n)
    l = len(n)
    srt = n[:]
    while True:
        cnt = 0
        for i in range(l-1):
            if srt[i] > srt[i+1]:
                srt[i], srt[i+1] = srt[i+1], srt[i]
            else:
                cnt += 1
        if cnt == l-1:
            break
    d = 0
    while not srt[d]:
        d += 1
    mn = srt[d]
    print(f'#{case}', mini(), maxi())


# T = int(input())
# for tc in range(1, T + 1):
#     N = input()
#     lst = list(map(int, N))
#     n = len(lst)
#     mx = mn = int(N)
#     for i in range(n):
#         for j in range(i, n):
#             lst[i], lst[j] = lst[j], lst[i]
#             if lst[0] != 0:
#                 new_N = 0
#                 k = 0
#                 t = n - 1
#                 while t>=0:
#                     new_N += lst[t] * (10**k)
#                     k += 1
#                     t -= 1
#                 if new_N > mx:
#                     mx = new_N
#                 if new_N < mn:
#                     mn = new_N
#             lst[i], lst[j] = lst[j], lst[i]
#     print(f'#{tc} {mn} {mx}')