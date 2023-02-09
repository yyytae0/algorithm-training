garo, sero = map(int, input().split())
s = int(input())
loc = [list(map(int, input().split())) for _ in range(s)]  # 1:상, 2:하, 3:좌, 4:우
D_dir, D_loc = map(int, input().split())

lst = [[0] * (garo + 1) for _ in range(sero + 1)]

s_lst = []
for k in loc:
    if k[0] == 1:
        s_lst.append([0, k[1]])
    elif k[0] == 2:
        s_lst.append([sero, k[1]])
    elif k[0] == 3:
        s_lst.append([k[1], 0])
    elif k[0] == 4:
        s_lst.append([k[1], garo])
# print(s_lst)

for i in range(sero + 1):
    for j in range(garo + 1):
        if i == 0 or i == sero or j == 0 or j == garo:
            lst[i][j] = 1

if D_dir == 1:
    target = [0, D_loc]
elif D_dir == 2:
    target = [sero, D_loc]
elif D_dir == 3:
    target = [D_loc, 0]
elif D_dir == 4:
    target = [D_loc, garo]

# print(s_lst)
# print(*lst, sep="\n")

di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]
final = 0

for idx in s_lst:
    i = idx[0]
    j = idx[1]
    if i == 0:
        dr = 0
    elif i == sero:
        dr = 2
    elif j == 0:
        dr = 3
    elif j == garo:
        dr = 1

    cnt = 0
    while True:
        ni, nj = i + di[dr], j + dj[dr]
        if (0 <= ni <= sero) and (0 <= nj <= garo) and (lst[ni][nj]) != 0:
            i, j = ni, nj
            cnt += 1
            if [ni, nj] == target:
                break
        else:  # 방향 꺾기
            dr = (dr + 1) % 4  # 0-1-2-3-0-1-2-...

    final = final + min((garo * 2 + sero * 2) - cnt, cnt)

    # print(final)
print(final)
