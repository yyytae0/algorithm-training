ip = int(input())
lst = list()

for i in range(ip):
    friend = list(input())
    lst.append(friend)
max = 1
cnt_lst = list()
for i in range(ip):
    for j in range(ip):
        if lst[i][j] == 'Y':
            if j not in cnt_lst:
                cnt_lst.append(j)

            for k in range(ip):
                if lst[j][k] == 'Y':
                    if k not in cnt_lst:
                        cnt_lst.append(k)

    if len(cnt_lst) > max:
        max = len(cnt_lst)

    cnt_lst = []

print(max-1)
