from sys import stdin
import collections

ip = int(stdin.readline())
total = 0
n_lst = list()
cnt = collections.Counter()
cnt_total = 0
most_cnt = 0
most_check = 0

for i in range(ip):
    n = int(stdin.readline())
    n_lst.append(n)
    total = total + n
    cnt[n] += 1
    if cnt[n] > most_cnt:
        most_cnt = cnt[n]
        most_check = 1
    elif cnt[n] == most_cnt:
        most_check += 1
    cnt_total += 1


a = cnt.most_common(most_check)
a.sort()
n_lst.sort()
print(round(total/cnt_total))
print(n_lst[cnt_total//2])
if len(a) != 1:
    print(a[1][0])
else:
    print(a[0][0])

if cnt_total == 1:
    print(0)

else:
    print(n_lst[-1] - n_lst[0])
