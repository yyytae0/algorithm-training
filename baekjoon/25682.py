def check():
    answer = 4000000
    for i in range(n-k+1):
        for j in range(m-k+1):
            if i == 0 and j == 0:
                ans = cnt[k-1][k-1]

            elif i == 0:
                ans = cnt[k-1][k-1+j] - cnt[k-1][j-1]

            elif j == 0:
                ans = cnt[k+i-1][k-1] - cnt[i-1][k-1]

            else:
                ans = cnt[k+i-1][k+j-1] - cnt[k+i-1][j-1] - cnt[i-1][k+j-1] + cnt[i-1][j-1]
            answer = min(ans, k**2 - ans, answer)
    return answer


n, m, k = map(int, input().split())
lst = list()
for i in range(n):
    lst.append(input())

c = ['W', 'B']
s1 = ''
s2 = ''
dummy = 0
for i in range(m):
    s1 = s1 + c[dummy]
    s2 = s2 + c[1-dummy]
    dummy = 1 - dummy
s = [s1, s2]
cnt = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    dummy = 1-dummy
    for j in range(m):
        if lst[i][j] == s[dummy][j]:
            y = 0
        else:
            y = 1
        if i == 0 and j == 0:
            cnt[i][j] = y
        elif i == 0:
            cnt[i][j] = y + cnt[i][j-1]
        elif j == 0:
            cnt[i][j] = y + cnt[i-1][j]
        else:
            cnt[i][j] = y + cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1]

print(check())
