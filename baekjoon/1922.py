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


n = int(input())
m = int(input())
lst = []
root = [i for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst.append([c, a, b])
lst.sort()
ans = 0
for i in lst:
    a = find(i[1])
    b = find(i[2])
    if a == b:
        continue
    else:
        union(a, b)
        ans += i[0]
print(ans)
