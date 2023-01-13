def square(length):
    area = length * length
    
    return area
    
    
    
ip = int(input())

for i in range(1, ip + 1):
    l = int(input())
    area = square(l)
    print("#%d %d" % (i, area))
