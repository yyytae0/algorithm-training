ip = int(input())

for case in range(1, ip+1):
    lst = list(map(int, input().split()))[1:]
    cnt = 0
    for i in range(20):
        for j in range(i):
            if lst[j] > lst[i]:
                d = lst[i]
                lst.remove(d)
                lst.insert(j, d)
                cnt += i-j
                break
    print(case, cnt)