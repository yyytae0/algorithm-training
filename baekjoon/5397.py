def check():
    idx = 0
    mx = 0
    ans = ''
    for i in a:
        if i == '<':
            if idx:
                idx -= 1
        elif i == '>':
            if idx != mx:
                idx += 1
        elif i == '-':
            if idx > 0:
                ans = ans[:idx-1] + ans[idx:]
                mx -= 1
        else:
            ans = ans[:idx] + i + ans[idx:]
            mx += 1
            idx += 1
    return ans


ip = int(input())

for case in range(ip):
    a = input()
    print(check())
