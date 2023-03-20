lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()
dp = []
for i in range(len(a)):
    dp.append(lst[ord(a[i])-65])
    dp.append(lst[ord(b[i])-65])
n = len(dp)
while n > 2:
    for idx in range(n):
        dp[idx] += dp[idx+1]
        if dp[idx] >= 10:
            dp[idx] -= 10
        if idx == n-2:
            dp.pop()
            n -= 1
            break
print(str(dp[0])+str(dp[1]))
