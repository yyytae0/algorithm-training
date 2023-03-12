ip = int(input())

for i in range(1, ip+1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.append(n)
    dummy = []
    charge = [0]
    ans = 1
    for j in lst:
        if charge[-1] + k > j:
            dummy.append(j)

        elif charge[-1] + k == j:
            if j == n:
                break
            dummy = []
            charge.append(j)

        else:
            if dummy:
                charge.append(dummy[-1])
                if dummy[-1] + k < j:
                    ans = 0
                    break

                else:
                    dummy.append(j)

            else:
                ans = 0
                break

    if ans:
        print(f'#{i} {len(charge)-1}')

    else:
        print(f'#{i} 0')
