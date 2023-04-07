page = int(input())
n = len(str(page))
ans_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, page + 1):
    num_str = str(i)
    for j in range(10):
        ans_lst[j] += num_str.count(str(j))

print(*ans_lst)


dp = [[0 for _ in range(10)] for _ in range(10)]
dp[1] = [1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
