n, J, H = map(int, input().split())
cnt = 0

while J != H:
    if J % 2 == 0:
        J = J/2

    elif J % 2 == 1:
        J = (J+1)/2

    if H % 2 == 0:
        H = H/2

    elif H % 2 == 1:
        H = (H+1)/2

    cnt += 1

print(cnt)
