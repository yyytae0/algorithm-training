def check(st):
    left = [0]
    for i in st:
        if i == '(' or i == '[':
            left.append(i)

        elif i == ')':
            dummy = left.pop()
            if dummy == '[' or dummy == 0:
                return False

        elif i == ']':
            dummy = left.pop()
            if dummy == '(' or dummy == 0:
                return False

    if left.pop() == 0:
        return True

    else:
        return False


while True:
    ip = input()
    if ip == '.':
        break

    if check(ip):
        print('yes')

    else:
        print('no')
