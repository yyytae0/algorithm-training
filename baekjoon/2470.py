n = int(input())
lst = list(map(int, input().split()))
lst.sort()
s = 0
g = n-1
target = 10**9
if lst[s] > 0:
    t = [0, 1]
elif lst[g] < 0:
    t = [-2, -1]
else:
    while True:
        dummy = lst[s] + lst[g]
        if lst[s] > 0 or lst[g] < 0:
            if abs(dummy) < target:
                target = abs(dummy)
                t = [s, g]
            break
        if abs(dummy) < target:
            target = abs(dummy)
            t = [s, g]

        if dummy == 0:
            ans = [s, g]
            break
        elif dummy > 0:
            g = g - 1
        elif dummy < 0:
            s = s + 1
        if s >= g:
            break

print(lst[t[0]], lst[t[1]])
