def make():
    if n >= 1:
        print(1)
    if n >= 2:
        print(1, 1)
    if n >= 3:
        now = [1, 1]
        for i in range(2, n):
            dummy = now[:]
            now = [1]
            for j in range(i-1):
                now.append(dummy[j]+dummy[j+1])
            now.append(1)
            print(*now)


ip = int(input())
for case in range(1, ip+1):
    n = int(input())
    print(f'#{case}')
    make()
