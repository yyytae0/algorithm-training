def solution(lst):
    n = len(lst)
    m = len(lst[0])
    dp = [[[0 for _ in range(26)] for _ in range(m)] for _ in range(n)]
    for i in range(n): # dp 배열 설정(i, j 좌표까지 알파벳별 횟수)
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j][ord(lst[i][j])-65] = 1
            else:
                for k in range(26):
                    if i == 0:
                        dp[i][j][k] = dp[i][j-1][k]
                    elif j == 0:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i][j - 1][k] - dp[i - 1][j - 1][k]
                dp[i][j][ord(lst[i][j])-65] += 1
    ans = 10**4
    for i in range(n-1):
        for j in range(m-1):
            # 구역을 나누는 기준점 i, j
            ans = min(ans, check(i, j, dp, n, m))
    print(ans)
    return ans


def check(a, b, dp, n, m):
    # 기준점 a, b를 기준으로 4개 구역 알파벳 별 횟수
    chk1 = dp[a][b][:]
    chk2 = [0 for _ in range(26)]
    chk3 = [0 for _ in range(26)]
    chk4 = [0 for _ in range(26)]
    for i in range(26):
        chk2[i] = dp[a][m-1][i] - dp[a][b][i]
        chk3[i] = dp[n-1][b][i] - dp[a][b][i]
        chk4[i] = dp[n-1][m-1][i] - dp[a][m-1][i] - dp[n-1][b][i] + dp[a][b][i]
    sm1 = sum(chk1)
    sm2 = sum(chk2)
    sm3 = sum(chk3)
    sm4 = sum(chk4)
    total = sm1 + sm2 + sm3 + sm4
    mn = 10**4
    for i in range(26):
        for j in range(26):
            if i != j and mn > chk1[i]+chk2[j]:
                for k in range(26):
                    if i != k and mn > chk1[i]+chk2[j]+chk3[k]:
                        for l in range(26):
                            if j != l and k != l:
                                d = total - chk1[i] - chk2[j] - chk3[k] - chk4[l]
                                mn = min(mn, d)
    return mn


a = ['AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA','AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAA']
solution(a)
