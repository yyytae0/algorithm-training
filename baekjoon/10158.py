w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (t % (2*w)) + p
y = (t % (2*h)) + q

if x > w:
    x -= w
    if x > w:
        x -= w

    else:
        x = w - x

if y > h:
    y -= h
    if y > h:
        y -= h

    else:
        y = h - y

print(x, y)
