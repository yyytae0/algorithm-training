class Ent:
    global w
    global h

    def __init__(self, x, y, way_x=1, way_y=1):
        self.x = x
        self.y = y
        self.way_x = way_x
        self.way_y = way_y

    def move(self):
        if self.way_x == 1:
            if self.x+1 > w:
                self.x -= 1
                self.way_x = -1
            else:
                self.x += 1

        elif self.way_x == -1:
            if self.x-1 < 0:
                self.x += 1
                self.way_x = 1
            else:
                self.x -= 1

        if self.way_y == 1:
            if self.y+1 > h:
                self.y -= 1
                self.way_y = -1
            else:
                self.y += 1

        elif self.way_y == -1:
            if self.y-1 < 0:
                self.y += 1
                self.way_y = 1
            else:
                self.y -= 1


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
a = Ent(p, q)
cnt = 0
a_dict = dict()
a_dict[0] = [a.x, a.y]
while True:
    a.move()
    cnt += 1
    a_dict[cnt] = [a.x, a.y]
    if (a.x, a.y, a.way_x, a.way_y) == (p, q, 1, 1):
        break

    if cnt == t:
        break

while t > cnt:
    t = t - cnt

print(*a_dict[t])
