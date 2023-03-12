ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    x = int(n ** (1/3) + 0.00000001)
    if x**3 == n:
        print(f'#{case} {x}')
    else:
        print(f'#{case} -1')
