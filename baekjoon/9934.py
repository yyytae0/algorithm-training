from collections import deque


def check(a):
    if a >= 2**(k-1):
        lst[a-1] = q.popleft()
        return
    check(a*2)
    lst[a-1] = q.popleft()
    check(a*2+1)


k = int(input())
q = deque(list(map(int, input().split())))
lst = [0 for _ in range(2**k-1)]
check(1)
cnt = 1
for i in lst:
    cnt += 1
    print(i, end=' ')
    for j in range(1, 11):
        if cnt == 2**j:
            print()
            break
        elif cnt < 2**j:
            break
