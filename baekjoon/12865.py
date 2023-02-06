n, k = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = [[0 for _ in range(n+1)] for _ in range(k+1)]
#
# for i in range(k+1):
#     for j in range(n+1):
#         if i
