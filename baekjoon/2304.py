from sys import stdin

ip = int(stdin.readline())
lst = list()
high_lst = []
high = (0, 0)
for i in range(ip):
    lst.append(list(map(int, stdin.readline().split())))
    if lst[-1][1] > high[1]:
        high_lst = [lst[-1]]
        high = lst[-1]

    elif lst[-1][1] == high[1]:
        high_lst.append(lst[-1])

high_lst.sort()
lst.sort()
cnt = 0
ans = 0
height = lst[0][1]
width = lst[0][0]

while True:
    if lst[cnt][1] > height:
        ans = ans + height*(lst[cnt][0]-width)
        height = lst[cnt][1]
        width = lst[cnt][0]

    if lst[cnt][1] == high[1]:
        break

    cnt += 1

lst.sort(reverse=True)
height = lst[0][1]
width = lst[0][0]
cnt = 0
while True:
    if lst[cnt][1] > height:
        ans = ans + height * (width - lst[cnt][0])
        height = lst[cnt][1]
        width = lst[cnt][0]

    if lst[cnt][1] == high[1]:
        break

    cnt += 1

if len(high_lst) == 1:
    ans = ans + high_lst[0][1]

else:
    ans = ans + (high_lst[-1][0] - high_lst[0][0] + 1)*high_lst[0][1]

print(ans)
