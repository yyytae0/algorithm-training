def check(word):
    dummy = word[0]
    check_lst = list()
    check_lst.append(word[0])
    for i in word:
        if i == dummy:
            continue

        else:
            if i in check_lst:
                return False

            else:
                dummy = i
                check_lst.append(i)

    return True


ip = int(input())
cnt = 0

for i in range(ip):
    word = input()
    if check(word):
        cnt += 1

print(cnt)
