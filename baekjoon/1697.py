def find(start, arrive):
    if start == arrive:
        return True

    elif arrive % 2 == 1:
        find(start, arrive + 1)
        find(start, arrive - 1)

    else:
        if start <= (arrive/2):
            find(start, arrive/2)

        else:
            pass


# ip = list(map(int, input().split()))
# now = ip[0]
# cnt = 0
#
# while True:
#     if now * 2 > ip[1]:
#         if now*2-ip[1] > ip[1]-now:
#             cnt = cnt + ip[1] - now
#
#         else:
#             cnt = cnt + now*2 - ip[1] + 1
#         break
#
#     elif now == ip[1]:
#         break
#
#     else:
#         now = now * 2
#         cnt += 1
#
# print(cnt)
