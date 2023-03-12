ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input()))
    card = dict()
    for j in range(10):
        card[j] = 0

    for j in lst:
        card[j] += 1

    mx = [0, 0]
    for j in range(10):
        if card[j] > mx[1]:
            mx = [j, card[j]]

        if card[j] == mx[1]:
            if j > mx[0]:
                mx = [j, card[j]]

    print(f'#{i}', *mx)
