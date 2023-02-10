def lotto(lst, k, n, dummy):
    global ans
    if len(dummy) == 6:
        ans.append(dummy[:])
        return

    for i in range(n, k):
        dummy.append(lst[i])
        lotto(lst, k, i+1, dummy)
        dummy.pop()


while True:
    ip = input()
    if ip[0] == '0':
        break
    lst = list(map(int, ip.split()))
    k = lst[0]
    lst = lst[1:]
    ans = []
    dummy = []
    lotto(lst, k, 0, dummy)
    for i in ans:
        print(*i)
    print()
# 25% 실패
