ip = int(input())

for case in range(1, ip+1):
    a, b = input().split()
    n_a = len(a)
    n_b = len(b)
    idx = 0
    dummy = 0
    cnt = 0
    while idx < n_a:
        if a[idx] == b[0]:
            if idx + n_b - 1 < n_a:
                for i in range(n_b):
                    if a[idx + i] != b[i]:
                        dummy = 1
                        break
                if dummy == 1:
                    dummy = 0

                else:
                    idx = idx + n_b - 1
        idx += 1
        cnt += 1
    print(f'#{case} {cnt}')
