ip = list(map(int, input().split()))
min_set = 1000
min_solo = 1000
cnt = 6

for i in range(ip[1]):
    cost = list(map(int, input().split()))
    if cost[0] < min_set:
        min_set = cost[0]

    if cost[1] < min_solo:
        min_solo = cost[1]

for i in range(1, 7):
    if i * min_solo > min_set:
        cnt = i-1

onlyset = ((ip[0]//6) + 1) * min_set
onlysolo = ip[0] * min_solo
mix = (ip[0]//6) * min_set + (ip[0] % 6) * min_solo

print(min(onlyset, onlysolo, mix))
