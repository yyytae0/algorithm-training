paper = list(map(int, input().split()))
ip = int(input())
lst0 = [0, paper[1]]
lst1 = [0, paper[0]]
for i in range(ip):
    code, n = map(int, input().split())
    if code == 0:
        lst0.append(n)

    elif code == 1:
        lst1.append(n)

lst0.sort()
lst1.sort()
max0 = 0
max1 = 0
for i in range(1, len(lst0)):
    dummy0 = lst0[i]-lst0[i-1]
    if dummy0 > max0:
        max0 = dummy0

for i in range(1, len(lst1)):
    dummy1 = lst1[i] - lst1[i - 1]
    if dummy1 > max1:
        max1 = dummy1

print(max0*max1)
