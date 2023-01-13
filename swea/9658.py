def round(num):
    a = str(num)
    b = len(a) - 1
    c = int(a[0:2])
    ans = list()
    
    if int(a[2]) >= 5:
        c += 1
        if c == 100:
            b += 1
        
    
    d = str(c)
    ans.append(d)
    ans.append(b)
    
    return ans


ip = int(input())

for i in range(1, ip + 1):
    num = int(input())
    lst = round(num)
    print("#%d %s.%s*10^%d" % (i, lst[0][0], lst[0][1], lst[1]))

