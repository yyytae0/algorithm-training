ip = int(input())

for i in range(1, ip+1):
    n, d = map(int, input().split())
    lst = list(map(int, input().split()))
    start = 0
    last = n
    while True:
        idx = (start+last)//2
        if d == lst[idx]:
            print(f'#{i} {idx+1}')
            break

        elif start >= last:
            print(f'#{i} 0')
            break

        elif d > lst[idx]:
            start = idx + 1
            pass

        elif d < lst[idx]:
            last = idx - 1
            pass
