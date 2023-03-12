def check(a):
    global ans, cnt
    if sum(ans) == k:
        cnt += 1
        return
    if sum(ans) > k:
        return
    for i in range(a+1, n):
        ans.append(lst[i])
        check(i)
        ans.pop()


ip = int(input())

for case in range(1, ip+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = list()
    cnt = 0
    check(-1)
    print(f'#{case} {cnt}')
