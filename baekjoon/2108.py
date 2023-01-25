from sys import stdin

ip = int(stdin.readline())
min_n = 4000
max_n = -4000
total = 0
n_lst = list()
n_dict = dict()
cnt = 0

for i in range(ip):
    n = int(stdin.readline())
    n_lst.append(n)
    total = total + n
    cnt += 1
    if n not in n_dict.keys():
        n_dict[n] = 1

    else:
        n_dict[n] = n_dict[n] + 1

n_lst.sort()

