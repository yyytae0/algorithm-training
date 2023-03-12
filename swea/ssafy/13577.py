def check(lst):
    cnt = dict()
    for i in range(10):
        cnt[i] = 0
    dummy = 0
    # 입력된 숫자 하나씩 카운트
    for i in lst:
        cnt[i] += 1

    # 같은숫자 3개씩 판별
    for i in lst:
        if cnt[i] == 6:
            return True

        elif cnt[i] >= 3:
            cnt[i] -= 3
            dummy += 1

    # 연속된 숫자판별
    for i in cnt.keys():
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            dummy += 1

        if dummy == 2:
            return True

    return False


ip = int(input())

for i in range(1, ip+1):
    lst = list(map(int, input()))
    if check(lst):
        print(f'#{i} 1')

    else:
        print(f'#{i} 0')
