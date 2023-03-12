ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    idx = m % n
    print(f'#{case} {lst[idx]}')
