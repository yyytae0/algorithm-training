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
    k = int(ip[0])
    lst = list(map(int, ip[1:].split()))
    ans = []
    dummy = []
    lotto(lst, k, 0, dummy)
    for i in ans:
        print(*i)
    print()
