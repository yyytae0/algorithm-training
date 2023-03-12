def check():
    mx = 0
    for i in range(100):
        for j in range(100):
            for k in range(100-j, mx, -1):
                for n in range(k//2):
                    if lst[i][j+n] != lst[i][j+k-n-1]:
                        break
                else:
                    if k > mx:
                        mx = k
                        break
                for n in range(k//2):
                    if lst[j+n][i] != lst[j+k-n-1][i]:
                        break
                else:
                    if k > mx:
                        mx = k
                        break
    return mx


for _ in range(10):
    case = int(input())
    lst = list(input() for _ in range(100))
    ans = check()
    print(f'#{case} {ans}')
