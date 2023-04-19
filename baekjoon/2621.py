def cnt():
    flag, flag2, flag3 = 0, 0, 0
    for i in range(1, 10):
        if nums[i] == 4:
            return 800 + i
        elif nums[i] == 3:
            if flag2:
                return i*10 + flag2 + 700
            flag3 = i
        elif nums[i] == 2:
            if flag3:
                return flag3*10 + i + 700
            elif flag2:
                return max(flag2, i)*10 + min(flag2, i) + 300
            flag2 = i
        elif not flag and nums[i] == 1:
            if i+4 < 10 and nums[i+1] and nums[i+2] and nums[i+3] and nums[i+4]:
                return 500 + i+4
            flag = 1
        if flag and nums[i]:
            flag = i
    if flag3:
        return 400 + flag3
    elif flag2:
        return 200 + flag2
    else:
        return 100 + flag


def check():
    d = cnt()
    for i in color:
        if color[i] == 5:
            if 500 < d < 600:
                return 900 + d - 500
            return 600 + d - 100
        elif color[i]:
            return d


color = {'B': 0, 'Y': 0, 'R': 0, 'G': 0}
nums = [0 for _ in range(10)]

for i in range(5):
    a, b = input().split()
    color[a] += 1
    nums[int(b)] += 1

print(check())