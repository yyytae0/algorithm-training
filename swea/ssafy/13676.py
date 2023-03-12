ip = int(input())

for case in range(1, ip+1):
    p, a, b = map(int, input().split())

    start = 1
    last = p
    cnt_a = 1
    while True:
        target = int((start+last)/2)
        if target == a:
            break

        elif target > a:
            last = target

        elif target < a:
            start = target

        cnt_a += 1

    start = 1
    last = p
    cnt_b = 1
    while True:
        target = int((start + last) / 2)
        if target == b:
            break

        elif target > b:
            last = target

        elif target < b:
            start = target

        cnt_b += 1

        if cnt_b > cnt_a:
            break

    if cnt_a < cnt_b:
        print(f'#{case} A')

    elif cnt_b < cnt_a:
        print(f'#{case} B')

    elif cnt_b == cnt_a:
        print(f'#{case} 0')
