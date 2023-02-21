n = int(input())
lst = list(map(int, input().split()))
ans = [-1]
dummy = lst[-1]
dct = dict()
dct[lst[-1]] = -1
for i in range(2, n+1):
    if dummy > lst[-i]:
        ans.append(dummy)
        dct[lst[-i]] = dummy
        dummy = lst[-i]
    else:
        while dummy != -1:
            dummy = dct[dummy]
            if dummy > lst[-i]:
                ans.append(dummy)
                dct[lst[-i]] = dummy
                dummy = lst[-i]
                break
        if dummy == -1:
            ans.append(dummy)
            dct[lst[-i]] = dummy
        dummy = lst[-i]
print(*ans[::-1])
