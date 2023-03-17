n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = float('inf')
for i in range(n-k+1):
    for j in range(k, n-i+1):
        m = sum(lst[i:i+j])/j
        r = 0
        for s in range(j):
            r += (lst[i+s]-m)**2
        d = r/j
        if d < ans:
            ans = d
print(ans**(1/2))
