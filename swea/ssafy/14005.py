ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    box = list(map(int, input().split()))
    car = list(map(int, input().split()))
    box.sort(reverse=True)
    car.sort(reverse=True)
    idxc, idxb = 0, 0
    ans = 0
    while True:
        if box[idxb] <= car[idxc]:
            ans += box[idxb]
            idxb += 1
            idxc += 1
        else:
            idxb += 1
        if idxb == n or idxc == m:
            break
    print(f'#{case} {ans}')
