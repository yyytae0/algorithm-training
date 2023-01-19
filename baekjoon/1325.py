def trust(com, dct, trust_lst):
    if com not in trust_lst:
        trust_lst.append(com)
        for i in dct[com]:
            if i in dct.keys():
                trust_lst = trust(i, dct, trust_lst)

            else:
                trust_lst.append(i)

    else:
        pass

    return trust_lst


n, m = map(int, input().split())
hack = dict()
ans = list()
max_com = 0
com = list()

for i in range(m):
    ip = input().split()
    if ip[1] in hack.keys():
        hack[ip[1]].append(ip[0])

    else:
        hack[ip[1]] = list(ip[0])

for i in hack.keys():
    ans = trust(i, hack, ans)
    if len(ans) > max_com:
        max_com = len(ans)
        com = list()
        com.append(int(i))

    elif len(ans) == max_com:
        com.append(int(i))

    ans = []

print(*com)
