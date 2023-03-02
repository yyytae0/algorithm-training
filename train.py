import sys

sys.setrecursionlimit(10**5)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    flag, a, b = map(int, sys.stdin.readline().split())
    if flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)