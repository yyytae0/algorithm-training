import math


def init(left, right, node):
    if left == right:
        tree[node] = (lst[left-1], lst[left-1])
        return tree[node]
    mid = (left + right) // 2
    d1 = init(left, mid, node*2)
    d2 = init(mid+1, right, node*2 + 1)
    tree[node] = (min(d1[0], d2[0]), max(d1[1], d2[1]))
    return tree[node]


def find(left, right, node, lidx, ridx):
    global ans
    if right < lidx or ridx < left:
        return
    elif lidx <= left and right <= ridx:
        ans = (min(tree[node][0], ans[0]), max(tree[node][1], ans[1]))
        return
    mid = (left + right) // 2
    find(left, mid, node*2, lidx, ridx)
    find(mid+1, right, node*2+1, lidx, ridx)


n, m = map(int, input().split())
lst = list(int(input()) for _ in range(n))
tree = [(0, 0) for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(1, n, 1)
for i in range(m):
    a, b = map(int, input().split())
    ans = (float('inf'), 0)
    find(1, n, 1, a, b)
    print(*ans)
