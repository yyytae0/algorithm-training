ip = list(map(int, input().split()))
n = ip[0]
k = ip[1]
binary_n = bin(n)
binary_n = binary_n[2:]
len_bn = len(binary_n)
cnt_1 = binary_n.count('1')
cnt = cnt_1 - k
ans = list(binary_n)
dummy = 0

if cnt_1 <= k:
    print(0)

else:
    for i in range(len_bn-1, 0, -1):
        if cnt >= 0:
            if ans[i] == '1':
                ans[i] = 0
                cnt -= 1

            else:
                continue

        elif cnt == -1:
            if ans[i] == '0':
                cnt -= 1
                dummy = 1
                ans[i] = '1'
                break

    if cnt == -1:
        ans_num = 2 ** len_bn

    elif cnt == 0:
        ans_num = 2 ** len_bn

    elif dummy == 1:
        ans_num = 0
        for i in range(len_bn):
            if ans[i] == '1':
                ans_num = ans_num + 2 ** (len_bn - i - 1)

    print(int(ans_num) - n)