ip = input()
dummy = ''
lst = list()
for i in ip:
    if i == '+' or i == '-':
        lst.append(int(dummy))
        lst.append(i)
        dummy = ''

    else:
        dummy = dummy + i

lst.append(int(dummy))
ans = list()
cnt = 0
dummy = 0
for i in lst:
    if cnt == 0:
        if i == '+':
            continue

        elif i == '-':
            cnt = 1

        else:
            ans.append(i)
        pass

    elif cnt == 1:
        if i == '+':
            continue

        elif i == '-':
            ans.append(-dummy)
            dummy = 0

        else:
            dummy = dummy + i

ans.append(-dummy)
print(sum(ans))
