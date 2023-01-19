import sys

ip = list(sys.stdin.readline().strip())
ip.sort(reverse=True)
print(''.join(ip))
