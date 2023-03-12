ip = int(input())

for i in range(1, ip+1):
    n, m = map(int, input().split())
    lst_n = list(map(int, input().split()))
    lst_m = list(map(int, input().split()))

    if n == m:
        ans = 0
        for j in range(n):
            ans = ans + lst_n[j]*lst_m[j]

    elif n > m:
        ans = 0
        dummy = 0
        for j in range(n-m+1):
            dummy = 0
            for k in range(m):
                dummy = dummy + lst_n[k+j]*lst_m[k]

            if dummy > ans:
                ans = dummy

    else:
        ans = 0
        dummy = 0
        for j in range(m - n+1):
            dummy = 0
            for k in range(n):
                dummy = dummy + lst_n[k] * lst_m[k + j]

            if dummy > ans:
                ans = dummy

    print(f'#{i} {ans}')
