def solution(wallpaper):
    x_mn, y_mn, x_mx, y_mx = 50, 50, 0, 0
    for y, i in enumerate(wallpaper):
        for x, j in enumerate(i):
            if j == '#':
                if x > x_mx:
                    x_mx = x
                if x < x_mn:
                    x_mn = x
                if y > y_mx:
                    y_mx = y
                if y < y_mn:
                    y_mn = y
    answer = [y_mn, x_mn, y_mx+1, x_mx+1]
    return answer
