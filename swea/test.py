def binary(n, k):
    t = n + k
    max = 0
    min = 2**(t-1)

    if k == 0:
        for k in range(1, n + 1):
            max += 2 ** (t - k)

        min = max

    else:
        for i in range(1, n + 1):
            max += 2 ** (t - i)

        for j in range(n - 1):
            min += 2 ** (j)

    result = max * min

    return result


def cnt_binary(n):
    dummy = n
    cnt = 0
    while True:
        if (dummy % 2) == 1:
            if dummy == 1:
                break

            else:
                cnt += 1
                dummy = dummy // 2

        else:
            dummy = dummy//2

    return cnt


ip = int(input())

for i in range(ip):
    lst = list(map(int, input().split()))
    a = binary(lst[0], lst[1])
    b = cnt_binary(a)
    print(b)

