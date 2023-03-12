def check(a, b):
    if b == 1:
        return a
    ans = a * check(a, b-1)
    return ans


for case in range(1, 11):
    dummy = int(input())
    n, m = map(int, input().split())
    ans = check(n, m)
    print(f'#{case} {ans}')
