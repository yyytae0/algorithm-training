import sys


def postorder(a):
    global ans
    dummy = []
    for i in dct[a]:
        postorder(i[0])
        dummy.append(lst[i[0]] + i[1])
    if dummy:
        for i in range(len(dummy)):
            for j in range(i+1, len(dummy)):
                if dummy[i] + dummy[j] > ans:
                    ans = dummy[i] + dummy[j]
        lst[a] = max(dummy)
    else:
        lst[a] = 0
    if lst[a] > ans:
        ans = lst[a]


sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
dct = dict()
lst = [0 for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    dct[i] = []
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    dct[a].append([b, c])
postorder(1)
print(ans)
