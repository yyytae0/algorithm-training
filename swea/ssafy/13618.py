ip = int(input())

for i in range(1, ip+1):
    stop = dict()
    n = int(input())
    lst = list()
    for j in range(n):
        a, b = map(int, input().split())
        for k in range(a, b+1):
            if stop.get(k) is None:
                stop[k] = 1

            else:
                stop[k] += 1

    p = int(input())
    ans = list()
    for j in range(p):
        ans.append(stop[int(input())])

    print(f'#{i}', *ans)
