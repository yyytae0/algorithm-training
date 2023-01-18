ip = list(map(int, input().split()))
if ip[0] != 0:
    score = list(map(int, input().split()))
ans = 0

n = ip[0]
my = ip[1]
p = ip[2]

if ip[0] == 0:
    ans = 1

elif (len(score) < p) or (my > score[-1]):
    if my not in score:
        score.append(my)
        score.sort(reverse=True)

    for i in range(len(score)):
        if score[i] == my:
            ans = i + 1
            break

else:
    ans = -1

print(ans)
