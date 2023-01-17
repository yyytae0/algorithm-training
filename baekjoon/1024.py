ip = list(map(int, input().split()))
ans_lst = []
max = 101

if ip[1] < max:
    max = ip[0]

for i in range(ip[1], max):
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

if ans_lst == []:
    print('-1')

else:
    ans_lst.sort()
    print(*ans_lst)

