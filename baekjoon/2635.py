def make(a, b):
    lst = [a, b]
    idx = 1
    while True:
        if lst[idx-1]-lst[idx] >= 0:
            lst.append(lst[idx-1] - lst[idx])
            idx += 1

        else:
            return idx, lst


n = int(input())
mx = 0
for i in range(n//2, n+1):
    idx, lst = make(n, i)
    if idx > mx:
        mx = idx
        dummy = lst

print(mx+1)
print(*dummy)
