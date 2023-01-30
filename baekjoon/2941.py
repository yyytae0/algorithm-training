ip = list(input())
idx = 0
cnt = 0
idx_max = len(ip)

while True:
    if ip[idx] == 'c':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == '=' or ip[idx] == '-':
            idx += 1

    elif ip[idx] == 'd':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == '-':
            idx += 1

        elif ip[idx] == 'z':
            idx += 1
            cnt += 1
            if idx >= idx_max:
                break

            if ip[idx] == '=':
                idx += 1
                cnt -= 1

    elif ip[idx] == 'l' or ip[idx] == 'n':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == 'j':
            idx += 1

    elif ip[idx] == 's' or ip[idx] == 'z':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == '=':
            idx += 1

    else:
        idx += 1
        cnt += 1

    if idx >= idx_max:
        break

print(cnt)
