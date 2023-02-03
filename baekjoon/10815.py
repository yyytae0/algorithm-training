n = int(input())
lst_n = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))

ans = []
dct = dict()
for i in lst_n:
    dct[i] = 1

for i in lst_m:
    try:
        if dct[i] == 1:
            ans.append(1)

    except KeyError:
        ans.append(0)

print(*ans)
