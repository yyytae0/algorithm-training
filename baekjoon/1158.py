ip = list(map(int, input().split()))
lst = [i for i in range(1, ip[0]+1)]
ans_lst = list()
idx = ip[1]

while True:
    ans_lst.append(lst.pop(idx-1))
    if len(lst) == 0:
        break
    idx = idx - 1 + ip[1]
    if idx > len(lst):
        while idx >= len(lst):
            idx = idx - len(lst)

print(f'<{str(ans_lst)[1:-1]}>')
