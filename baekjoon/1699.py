# n = int(input())
# cnt = 0
# while n != 1:
#     a = int(n ** (1 / 2))
#     n = n - a ** 2
#     if n == 0:
#         break
#     cnt += 1
#
# print(cnt+1)
n = int(input())
lst = []
for i in range(int(n**(1/2))):
    lst.append(i**2)
print(len(lst))
