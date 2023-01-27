n, cost = map(int, input().split())
lst = list()
for i in range(n):
    coin = int(input())
    if coin <= cost:
        lst.append(coin)

total = 0
for i in range(1, len(lst)+1):
    total = total + (cost//lst[-i])
    cost = cost % lst[-i]
    if cost == 0:
        break

print(total)
