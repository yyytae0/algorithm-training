n, m = map(int, input().split())
cost = list()
income = 0
cnt = 0
sell_cost = 0

for i in range(m):
    cost.append(int(input()))

cost.sort(reverse=True)

while n > 0:
    if cnt >= m:
        break

    else:
        if cost[cnt] * (cnt + 1) > income:
            income = cost[cnt] * (cnt + 1)
            sell_cost = cost[cnt]
            n -= 1
            cnt += 1
        else:
            n -= 1
            cnt += 1

print(sell_cost, income)
