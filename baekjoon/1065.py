ip = int(input())

if ip < 100:
    cnt = ip

elif ip > 999:
    cnt = 144

else:
    cnt = 99
    for i in range(100, ip + 1):
        num_str = str(i)
        a = int(num_str[0])
        b = int(num_str[1])
        c = int(num_str[2])
        if (a - b) == (b - c):
            cnt += 1

        else:
            continue

print(cnt)
