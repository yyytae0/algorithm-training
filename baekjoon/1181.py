ip = int(input())
lst = list()
ans_lst = list()
len_lst = list()
key_lst = list()
d = dict()

for i in range(ip):
    dummy = input()
    if dummy in lst:
        continue
    lst.append(dummy)
    len_lst.append(len(dummy))
    if len(dummy) in key_lst:
        pass
    else:
        key_lst.append(len(dummy))

key_lst.sort()

for i in range(len(lst)):
    if len_lst[i] in d.keys():
        d[len_lst[i]].append(lst[i])
        d[len_lst[i]].sort()

    else:
        d[len_lst[i]] = []
        d[len_lst[i]].append(lst[i])

for i in key_lst:
    ans_lst = ans_lst + d[i]

for i in ans_lst:
    print(i)
