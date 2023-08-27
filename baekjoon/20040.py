from sys import stdin


def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        root[a] = b
    else:
        root[b] = a


def check():
    for i in range(m):
        a, b = map(int, stdin.readline().split())
        if find(a) == find(b):
            return i+1
        union(a, b)
    return 0


n, m = map(int, stdin.readline().split())
root = [i for i in range(n+1)]
print(check())