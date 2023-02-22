n = int(input())
lst = input()
lst = lst.replace('LL', 'LR')
dummy = 0
ans = 0
for i in lst:
    if dummy == 0:
        if i == 'S':
            ans += 1
        elif i == 'L':
            dummy = 1
            ans += 1
    elif dummy == 1:
        if i == 'S':
            ans += 1
        elif i == 'R':
            ans += 1
print(ans)
