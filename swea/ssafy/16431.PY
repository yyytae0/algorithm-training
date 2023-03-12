ip = int(input())

for case in range(1, ip+1):
    t = input()
    a1 = ''
    a2 = ''
    a3 = ''
    a4 = ''
    a5 = ''
    for i in t:
        a1 = a1 + '..#.'
        a2 = a2 + '.#.#'
        a3 = a3 + f'#.{i}.'
        a4 = a4 + '.#.#'
        a5 = a5 + '..#.'
    a1 = a1 + '.'
    a2 = a2 + '.'
    a3 = a3 + '#'
    a4 = a4 + '.'
    a5 = a5 + '.'
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
