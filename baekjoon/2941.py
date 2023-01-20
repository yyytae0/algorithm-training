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

        if ip[idx] == '=' or '-':
            idx += 1

    elif ip[idx] == 'd':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == '-':
            idx += 1
            if idx >= idx_max:
                break

        elif ip[idx] == 'z':
            idx += 1
            if idx >= idx_max:
                break

            if ip[idx] == '=':
                idx += 1
                if idx >= idx_max:
                    break

    elif ip[idx] == 'l' or 'n':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == 'j':
            idx += 1
            if idx >= idx_max:
                break

    elif ip[idx] == 's' or 'z':
        idx += 1
        cnt += 1
        if idx >= idx_max:
            break

        if ip[idx] == '=':
            idx += 1
            if idx >= idx_max:
                break

    else:
        idx += 1
        cnt += 1

    if idx > idx_max-1:
        break

    print(cnt)


print(cnt)
