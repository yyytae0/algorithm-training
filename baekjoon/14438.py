import math
from sys import stdin, stdout


def init(left, right, node):
    if left == right:
        tree[node] = lst[left-1]
        return
    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = min(tree[node*2], tree[node*2+1])


def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return
    if idx < left or right < idx:
        return
    mid = (left + right) // 2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)
    tree[node] = min(tree[node*2], tree[node*2+1])


def find(left, right, node, lidx, ridx):
    global mn
    if right < lidx or ridx < left:
        return
    if lidx <= left <= ridx and lidx <= right <= ridx:
        mn = min(mn, tree[node])
        return
    mid = (left + right) // 2
    find(left, mid, node*2, lidx, ridx)
    find(mid+1, right, node*2+1, lidx, ridx)


n = int(stdin.readline())
tree = [float('inf') for _ in range(2**(math.ceil(math.log2(n)+1)))]
lst = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
init(1, n, 1)
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update(1, n, 1, b, c)
    else:
        mn = float('inf')
        find(1, n, 1, b, c)
        stdout.write(str(mn) + '\n')
