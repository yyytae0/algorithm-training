ip = input()
a = ip.replace('()', 'L')
total = 0
cnt = 0
for i in a:
    if i == '(':
        cnt += 1
    elif i == ')':
        cnt -= 1
        total += 1
    elif i == 'L':
        total += cnt

print(total)
