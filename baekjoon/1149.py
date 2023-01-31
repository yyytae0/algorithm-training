ip = int(input())
red = [0]
blue = [0]
green = [0]
for i in range(ip):
    r, g, b = map(int, input().split())
    red.append(r)
    blue.append(b)
    green.append(g)

for i in range(2, ip+1):
    red[i] = min(red[i] + blue[i - 1], red[i] + green[i - 1])
    blue[i] = min(blue[i] + red[i - 1], blue[i] + green[i - 1])
    green[i] = min(green[i] + red[i - 1], green[i] + blue[i - 1])

print(min(red[ip], blue[ip], green[ip]))
