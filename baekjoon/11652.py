from collections import Counter
from sys import stdin


n = int(stdin.readline())
lst = list(int(stdin.readline()) for _ in range(n))
a = Counter(lst)
mx_n, mx_num = 0, float('inf')
for i in a.most_common():
    if i[1] >= mx_n:
        if i[0] < mx_num:
            mx_num = i[0]
    else:
        break
print(mx_num)

