def check(a):
    return ord(a)-97


def make(a, cnt):
    global ans
    if cnt == m-5:
        d = learn()
        if ans < d:
            ans = d
        return

    for i in range(a+1, 26):
        if not k[i]:
            k[i] = 1
            make(i, cnt + 1)
            k[i] = 0


def learn():
    d = 0
    for i in lst:
        for j in i:
            if not k[check(j)]:
                break
        else:
            d += 1
    return d


n, m = map(int, input().split())
lst = list(input() for _ in range(n))
k = [0 for _ in range(26)]
k[check('a')], k[check('n')], k[check('t')], k[check('i')], k[check('c')] = 1, 1, 1, 1, 1
if m < 5:
    print(0)
else:
    ans = 0
    make(-1, 0)
    print(ans)
