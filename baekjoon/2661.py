def check(s, l):
    chk = []
    for i in range(l-1):
        if s[i] == s[-1]:
            chk.append(i)
    for i in chk:
        step = l - i - 2
        if i-step >= 0:
            for j in range(step+1):
                if s[i+1+j] != s[i-step+j]:
                    break
            else:
                return False
    return True


lst = ['1', '2', '3']
n = int(input())
dp = [[], []]
dp[1] = ['1']
for i in range(2, n+1):
    cnt = 0
    dp.append([])
    for k in dp[i-1]:
        for j in lst:
            if j != k[-1]:
                new = k + j
                if check(new, i):
                    dp[i].append(new)
                    cnt += 1
        if cnt > 2:
            break
print(dp[n][0])
