ip = list(map(int, input().split()))
ans_lst = []

for i in range(ip[1], 101, 2):
    if ip[0] % i == 0:
        for j in range(i):
            ans_lst. append((ip[0]/i)-(i//2)+j)