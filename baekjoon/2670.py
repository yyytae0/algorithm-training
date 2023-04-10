# n = int(input())
# dp = [0 for _ in range(n+1)]
# dp[0] = 1
# mx = 1
# for i in range(1, n+1):
#     a = float(input())
#     dp[i] = max(dp[i-1]*a, a)
# print(mx)
# print('%0.3f' % max(dp))
# print(f'{mx:.3f}')

# 4
# 6.1
# 4.3
# 0.5
# 6.1

# 80.002
#
N = int(input())
arr = list(float(input()) for _ in range(N))
for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))
