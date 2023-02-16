def solve(a, b):
    if b % 2:
        return solve(d, b//2) * solve(d, b//2) * a
    else:
        return solve(d, b//2) * solve(d, b//2)


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
solve(lst, m)
