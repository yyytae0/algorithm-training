def check():
    for i in range(mn, 0, -1):
        if mn % i == 0:
            for j in lst:
                if j % i != 0:
                    break
            else:
                return cnt(i)
    return


def cnt(a):
    ans = 0
    for i in range(n-1):
        ans += lst[i]//a - 1
    return ans


n = int(input())
lst = list(int(input()) for _ in range(n))
mn = 10**9
for i in range(n-1):
    lst[i] = lst[i+1] - lst[i]
    if lst[i] < mn:
        mn = lst[i]
lst[n-1] = 0
print(check())
