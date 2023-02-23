def preorder(a):
    preord.append(dct[a])
    if left[a]:
        preorder(change[left[a]])
    if right[a]:
        preorder(change[right[a]])


def inorder(a):
    if left[a]:
        inorder(change[left[a]])
    inord.append(dct[a])
    if right[a]:
        inorder(change[right[a]])


def postorder(a):
    if left[a]:
        postorder(change[left[a]])
    if right[a]:
        postorder(change[right[a]])
    postord.append(dct[a])


n = int(input())
left = ['' for _ in range(n)]
right = ['' for _ in range(n)]
dct = dict()
change = dict()
for i in range(n):
    a, b, c = input().split()
    dct[i] = a
    change[a] = i
    if b != '.':
        left[i] = b
    if c != '.':
        right[i] = c

preord = []
inord = []
postord = []

preorder(0)
inorder(0)
postorder(0)
print(''.join(preord))
print(''.join(inord))
print(''.join(postord))
