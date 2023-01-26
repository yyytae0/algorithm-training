num_dict = {0:1, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1}
new_dict = num_dict.copy()

ip = int(input())
ans = 0
if ip > 1:
    for i in range(ip-2):
        for j in num_dict:
            if j == 0:
                num_dict[j] = new_dict[j+1]

            elif j == 9:
                num_dict[j] = new_dict[j-1]

            else:
                num_dict[j] = new_dict[j-1] + new_dict[j+1]
        new_dict = num_dict.copy()

    for i in num_dict:
        if i == 0:
            continue

        else:
            ans = (ans + num_dict[i]) % 1000000000

else:
    ans = 9

print(ans % 1000000000)
