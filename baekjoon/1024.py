ip = list(map(int, input().split()))
ans_lst = []
max_l = 101
if ip[0] < max_l:
    if ip[0] > ip[1]:
        max_l = ip[0]

for i in range(ip[1], max_l):
    if i % 2 == 1:  # 홀수
        if ip[0] % i == 0:
            for j in range(i):
                if int((ip[0] / i) - (i // 2) + j) < 0:
                    ans_lst = []
                    break

                else:
                    ans_lst.append(int((ip[0] / i) - (i // 2) + j))

        if sum(ans_lst) != ip[0]:
            ans_lst = []
            continue
        break

    else:  # 짝수
        check = i // 2
        if ip[0] % check == 0:
            for j in range(check):
                if int(((ip[0] / check) // 2) - j) < 0:
                    ans_lst = []
                    break

                else:
                    ans_lst.append(int(((ip[0] / check) // 2) - j))
                    ans_lst.append(int(((ip[0] / check) // 2) + j + 1))

        if sum(ans_lst) != ip[0]:
            ans_lst = []
            continue
        break

if len(ans_lst) == 0:
    print('-1')

else:
    ans_lst.sort()
    print(*ans_lst)

