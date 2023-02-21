def solution(cap, n, deliveries, pickups):
    cnt1, cnt2 = 0, 0
    lst1 = []
    lst2 = []
    idx = n-1
    dummy = 0
    while idx > -1:
        if deliveries[idx] > dummy:
            deliveries[idx] -= dummy
            while deliveries[idx] > cap:
                lst1.append(idx + 1)
                cnt1 += 1
                deliveries[idx] -= cap
            dummy = cap - deliveries[idx]
            lst1.append(idx+1)
            cnt1 += 1
        elif deliveries[idx] > 0:
            dummy -= deliveries[idx]
        idx -= 1
    idx = n - 1
    dummy = 0
    while idx > -1:
        if pickups[idx] > dummy:
            pickups[idx] -= dummy
            while pickups[idx] > cap:
                lst2.append(idx + 1)
                pickups[idx] -= cap
                cnt2 += 1
            dummy = cap - pickups[idx]
            lst2.append(idx + 1)
            cnt2 += 1
        elif pickups[idx] > 0:
            dummy -= pickups[idx]
        idx -= 1
    ans = 0
    if cnt1 > cnt2:
        for i in range(cnt2):
            ans += max(lst1[i], lst2[i])
        for i in range(cnt2, cnt1):
            ans += lst1[i]
    else:
        for i in range(cnt1):
            ans += max(lst1[i], lst2[i])
        for i in range(cnt1, cnt2):
            ans += lst2[i]
    return ans*2


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)
