from sys import stdin, stdout


def check(a, now):
    if a > n:
        return
    lst[a] = now
    check(a*2, now)
    check(a*2+1, now)


n, q = map(int, stdin.readline().split())
lst = [0 for _ in range(n+1)]
for _ in range(q):
    a = int(stdin.readline())
    if lst[a]:
        stdout.write(str(lst[a]) + '\n')
    else:
        stdout.write('0\n')
        check(a, a)
