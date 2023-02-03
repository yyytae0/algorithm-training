ip = int(input())
for i in range(ip):
    k = int(input())
    n = int(input())
    ans = [_ for _ in range(1, n+1)]
    for j in range(k):
        for idx in range(1, n):
            ans[idx] = ans[idx] + ans[idx-1]

    print(ans[n-1])
