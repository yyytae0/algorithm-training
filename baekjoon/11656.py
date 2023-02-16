from sys import stdout


ip = input()
lst = list()
for i in range(len(ip)):
    lst.append(ip[i:])
lst.sort()
for i in lst:
    stdout.write(i+'\n')
