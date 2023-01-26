ip = int(input())
lst = list(map(int, input().split()))
condition = 1
cnt = 0
dummy = 0
max_cnt = 0
dummy_cnt = 0
for i in lst:
    if condition == 1:
        if i >= dummy:
            if i == dummy:
                dummy_cnt += 1

            else:
                dummy_cnt = 1
            dummy = i
            cnt += 1

        else:
            if cnt > max_cnt:
                max_cnt = cnt
            dummy = i
            cnt = dummy_cnt + 1
            condition = 0
            dummy_cnt = 1

    else:
        if i <= dummy:
            if i == dummy:
                dummy_cnt += 1

            else:
                dummy_cnt = 1
            dummy = i
            cnt += 1

        else:
            if cnt > max_cnt:
                max_cnt = cnt
            dummy = i
            cnt = dummy_cnt + 1
            condition = 1
            dummy_cnt = 1

if cnt > max_cnt:
    max_cnt = cnt

if ip == 1:
    max_cnt = 1

print(max_cnt)
