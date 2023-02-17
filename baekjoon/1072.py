# def check(a, b):
#     if 99*a <= 100*b:
#         return -1
#     else:
#         if a**2 % (99*a-100*b):
#             return a**2//(99*a-100*b) + 1
#         else:
#             return a**2//(99*a-100*b)
#
#
# a, b = map(int, input().split())
# ans = check(a, b)
# print(ans)


a, b = map(int, input().split())
p = (b*100)//a
if p >= 99:
    print(-1)
else:
    left = 1
    right = a
    while left <= right:
        mid = (left + right)//2
        if ((b+mid)*100)//(a+mid) > p:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
