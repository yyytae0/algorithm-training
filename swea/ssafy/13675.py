ip = int(input())

for i in range(1, ip+1):
    n, k = map(int, input().split())
    lst = [_ for _ in range(1, 13)]
    dummy = list()
    ans = 0
    for j in range(1 << 12):
        for m in range(12):
            if j & (1 << m):
                dummy.append(lst[m])

        if len(dummy) == n:
            if sum(dummy) == k:
                ans += 1
        
        dummy = []

    print(f'#{i} {ans}')


# def check(a, c):
#     global ans
#     if c == n:
#         if sum(d) == k:
#             ans += 1
#             return
#         else:
#             return
#     for i in range(a+1, 13):
#         d[c] = i
#         check(i, c+1)


# ip = int(input())

# for case in range(1, ip+1):
#     n, k = map(int, input().split())
#     d = [0 for _ in range(k)]
#     ans = 0
#     check(0, 0)
#     print(f'#{case} {ans}')
