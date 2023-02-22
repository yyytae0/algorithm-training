lst = list(map(int, input().split()))

while lst != [1, 2, 3, 4, 5]:
    for i in range(4):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            print(*lst)
