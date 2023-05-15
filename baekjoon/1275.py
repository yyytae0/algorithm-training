import math
from sys import stdin, stdout


def init(left, right, node):
    if left == right:
        tree[node] = lst[left-1]
        return tree[node]
    mid = (left + right) // 2
    tree[node] = init(left, mid, node*2) + init(mid+1, right, node*2+1)
    return tree[node]


def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return
    if idx < left or right < idx:
        return
    mid = (left + right) // 2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)
    tree[node] = tree[node*2] + tree[node*2+1]


def find(left, right, node, lidx, ridx):
    global sm
    if right < lidx or ridx < left:
        return
    elif lidx <= left <= ridx and lidx <= right <= ridx:
        sm += tree[node]
        return
    mid = (left + right) // 2
    find(left, mid, node*2, lidx, ridx)
    find(mid+1, right, node*2+1, lidx, ridx)


n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
tree = [0 for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(1, n, 1)
for i in range(m):
    a, b, c, d = map(int, stdin.readline().split())
    sm = 0
    a, b = min(a, b), max(a, b)
    find(1, n, 1, a, b)
    stdout.write(str(sm) + '\n')
    update(1, n, 1, c, d)
