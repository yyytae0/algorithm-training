import math
from sys import stdin, stdout


def init(left, right, node):
    if left == right:
        tree[node] = [left, lst[left-1]]
        return
    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    if tree[node*2][1] == tree[node*2+1][1]:
        tree[node] = tree[node*2][:]
    elif tree[node*2][1] < tree[node*2+1][1]:
        tree[node] = tree[node*2][:]
    else:
        tree[node] = tree[node*2+1][:]


def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node][1] = value
        return
    if idx < left or right < idx:
        return
    mid = (left + right) // 2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)
    if tree[node][1] > tree[node*2][1] or (tree[node][1] == tree[node*2][1] and tree[node][0] > tree[node*2][0]):
        tree[node] = tree[node*2][:]
    elif tree[node][1] > tree[node*2+1][1] or (tree[node][1] == tree[node*2+1][1] and tree[node][0] > tree[node*2+1][0]):
        tree[node] = tree[node*2+1][:]


def find(left, right, node, lidx, ridx):
    global mn, ans
    if right < lidx or ridx < left:
        return
    if lidx <= left <= ridx and lidx <= right <= ridx:
        if tree[node][1] < mn or (tree[node][1] == mn and tree[node][0] < ans):
            mn = tree[node][1]
            ans = tree[node][0]
        return
    mid = (left + right) // 2
    find(left, mid, node*2, lidx, ridx)
    find(mid+1, right, node*2+1, lidx, ridx)


n = int(stdin.readline())
tree = [[0, float('inf')] for _ in range(2**(math.ceil(math.log2(n)+1)))]
lst = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
init(1, n, 1)
print(tree)
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        print(tree)
        update(1, n, 1, b, c)
        print(tree)
    else:
        mn = float('inf')
        ans = 0
        find(1, n, 1, b, c)
        stdout.write(str(ans) + '\n')
