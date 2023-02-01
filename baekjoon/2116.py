from sys import stdin

# def check(lst):
#     for i in lst[-1]:
#         if i[0] in dummy or i[1] in dummy:
#             lst.pop()
#             check(lst)


ip = int(stdin.readline())
lst = list()

for i in range(ip):
    a, b, c, d, e, f = map(int, stdin.readline().split())
    lst.append([(a, f), (c, e), (b, d)])

print(lst)
