# from collections import deque
# import copy
#
#
# def bfs():
#     global visit, mn
#     tmp = copy.deepcopy(lst)
#     ans = 0
#     visit = [[0 for _ in range(n)] for _ in range(n)]
#     way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     q = deque()
#     for i in range(n):
#         for j in range(n):
#             if tmp[i][j] == 3:
#                 q.append([i, j, 0])
#                 visit[i][j] = 1
#     while q:
#         v = q.popleft()
#         for i in way:
#             nv = [v[0] + i[0], v[1] + i[1], v[2] + 1]
#             if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= n-1 and not visit[nv[0]][nv[1]]:
#                 q.append(nv)
#                 visit[nv[0]][nv[1]] = 1
#                 if tmp[nv[0]][nv[1]] == 1:
#                     ans += v[2] + 1
#     if ans < mn:
#         mn = ans
#
#
# def chick(cnt):
#     if cnt == 0:
#         bfs()
#         pass
#     for i in range(n):
#         for j in range(n):
#             if lst[i][j] == 2:
#                 lst[i][j] = 3
#                 chick(cnt - 1)
#                 lst[i][j] = 2
#
#
# n, m = map(int, input().split())
# lst = list(list(map(int, input().split())) for _ in range(n))
# visit = [[0 for _ in range(n)] for _ in range(n)]
# mn = 4000000
# chick(m)
# print(mn)

def check(cnt):
    global mn
    if cnt == 0:
        ans = 0
        for i in range(cnt1):
            dummy = []
            for j in lst3:
                dummy.append(dp[i][j])
            ans += min(dummy)
        if ans < mn:
            mn = ans
        return

    for i in range(cnt2):
        lst3.append(i)
        check(cnt-1)
        lst3.pop()


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
lst1 = list()
cnt1 = 0
lst2 = list()
cnt2 = 0
for i in range(n):
    for j in range(n):
        if lst[i][j] == 2:
            lst2.append([i, j])
            cnt2 += 1
        elif lst[i][j] == 1:
            lst1.append([i, j])
            cnt1 += 1

dp = [[0 for _ in range(cnt2)] for _ in range(cnt1)]
for i in range(cnt1):
    for j in range(cnt2):
        dp[i][j] = abs(lst1[i][0] - lst2[j][0]) + abs(lst1[i][1] - lst2[j][1])
mn = 4000000
lst3 = list()
check(m)
print(mn)
