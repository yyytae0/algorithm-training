a = input()
b = input()
while True:
    n = len(a)
    a = a.replace(b, '')
    if n == len(a):
        break
if n:
    print(a)
else:
    print('FRULA')