def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    root = [i for i in range(n+1)]
    for i in range(m):
        a = lst[2*i]
        b = lst[2*i+1]
        union(a, b)
    print(root)
    chk = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        a = find(i)
        chk[a] = 1
    ans = sum(chk)
    print(f'#{case} {ans}')
