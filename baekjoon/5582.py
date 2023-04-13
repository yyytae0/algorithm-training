a = input()
b = input()
na = len(a)
nb = len(b)
dp = [0 for _ in range(nb+1)]
mx = 0
for i in range(1, na+1):
    dummy = dp[:]
    for j in range(1, nb+1):
        if a[i-1] == b[j-1]:
            dp[j] = dummy[j-1] + 1
        else:
            dp[j] = 0
    mx = max(mx, max(dp))
print(mx)
