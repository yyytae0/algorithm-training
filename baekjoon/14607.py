n = int(input())
dp = 0
for i in range(2, n+1):
    dp = dp + (i-1) * 1
print(dp)

# dp = 0
# for i in range(n):
#     dp += i
# print(dp)
