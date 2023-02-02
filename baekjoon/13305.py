n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
idx = 0
ans = cost[0]*road[0]
now = 0
while True:
    while cost[now] <= cost[idx+1]:
        ans = ans + cost[now]*road[idx+1]
        idx += 1
        if idx > n-3:
            break

    if idx > n-3:
        break

    now = idx+1

print(ans)
