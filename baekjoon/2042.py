import math


def init(left, right, node):
    if left == right:
        tree[node] = lst[left-1]
        return
    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]


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


def query(left, right, node, lidx, ridx):
    global sm
    if ridx < left or right < lidx:
        return
    elif lidx <= left and right <= ridx:
        sm += tree[node]
        return
    elif lidx <= right or left <= ridx:
        mid = (left + right) // 2
        query(left, mid, node*2, lidx, ridx)
        query(mid+1, right, node*2+1, lidx, ridx)
        return


n, m, k = map(int, input().split())
lst = list(int(input()) for _ in range(n))
tree = [0 for _ in range(2**math.ceil(math.log2(n)+1))]
init(1, n, 1)
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, n, 1, b, c)
    else:
        sm = 0
        query(1, n, 1, b, c)
        print(sm)

