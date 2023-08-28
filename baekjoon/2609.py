a, b = map(int, input().split())
na, nb = a, b
if na < nb:
    na, nb = nb, na
while True:
    na, nb = nb, na % nb
    if nb == 0:
        break
print(na)
print(na*(a//na)*(b//na))
