def check(a):
    if tree[a] < tree[a//2]:
        tree[a], tree[a//2] = tree[a//2], tree[a]
        check(a//2)
    else:
        return


def make():
    for idx, i in enumerate(lst):
        tree[idx+1] = i
        check(idx+1)


def cnt(a):
    ans = 0
    while tree[a]:
        a = a // 2
        ans += tree[a]
    return ans


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    tree = [0 for _ in range(n+1)]
    make()
    ans = cnt(n)
    print(f'#{case} {ans}')
