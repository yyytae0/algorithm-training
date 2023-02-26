def check(lst):
    if ''.join(lst) in dummy:
        return False
    return True


def change():
    new = ['' for _ in range(n)]
    for i in range(n):
        new[rule[i]] = now[i]
    if check(new):
        dummy.append(''.join(new))
        return new
    else:
        return False


def stop(lst):
    if ''.join(lst) == ans:
        pass


n = int(input())
now = list(input().split())
rule = list(map(int, input().split()))
dummy = [''.join(now)]
ans = '012' * (n//3)
cnt = 0
while now:
    now = change()
    cnt += 1