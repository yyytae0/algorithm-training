map_index = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
reverse = {v: k for k, v in map_index.items()}

ip = input().split()
king_x = map_index[ip[0][0]]
king_y = int(ip[0][1])
stone_x = map_index[ip[1][0]]
stone_y = int(ip[1][1])
move_lst = []

for i in range(int(ip[2])):
    move = input()
    move_lst.append(move)

    if move == 'R':
        king_x += 1
        if king_x == stone_x and king_y == stone_y:
            stone_x += 1
            if stone_x == 9:
                stone_x -= 1
                king_x -= 1

        elif king_x == 9:
            king_x -= 1

    elif move == 'L':
        king_x -= 1
        if king_x == stone_x and king_y == stone_y:
            stone_x -= 1
            if stone_x == 0:
                stone_x += 1
                king_x += 1

        elif king_x == 0:
            king_x += 1

    elif move == 'B':
        king_y -= 1
        if king_x == stone_x and king_y == stone_y:
            stone_y -= 1
            if stone_y == 0:
                stone_y += 1
                king_y += 1

        elif king_y == 0:
            king_y += 1

    elif move == 'T':
        king_y += 1
        if king_x == stone_x and king_y == stone_y:
            stone_y += 1
            if stone_y == 9:
                stone_y -= 1
                king_y -= 1

        elif king_y == 9:
            king_y -= 1

    elif move == 'RT':
        king_x += 1
        king_y += 1
        if king_x == stone_x and king_y == stone_y:
            stone_x += 1
            stone_y += 1
            if stone_x == 9 or stone_y == 9:
                stone_x -= 1
                stone_y -= 1
                king_x -= 1
                king_y -= 1

        elif king_x == 9 or king_y == 9:
            king_x -= 1
            king_y -= 1

    elif move == 'LT':
        king_x -= 1
        king_y += 1
        if king_x == stone_x and king_y == stone_y:
            stone_x -= 1
            stone_y += 1
            if stone_x == 0 or stone_y == 9:
                stone_x += 1
                stone_y -= 1
                king_x += 1
                king_y -= 1

        elif king_x == 0 or king_y == 9:
            king_x += 1
            king_y -= 1

    elif move == 'RB':
        king_x += 1
        king_y -= 1
        if king_x == stone_x and king_y == stone_y:
            stone_x += 1
            stone_y -= 1
            if stone_x == 9 or stone_y == 0:
                stone_x -= 1
                stone_y += 1
                king_x -= 1
                king_y += 1

        elif king_x == 9 or king_y == 0:
            king_x -= 1
            king_y += 1

    elif move == 'LB':
        king_x -= 1
        king_y -= 1
        if king_x == stone_x and king_y == stone_y:
            stone_x -= 1
            stone_y -= 1
            if stone_x == 0 or stone_y == 0:
                stone_x += 1
                stone_y += 1
                king_x += 1
                king_y += 1

        elif king_x == 0 or king_y == 0:
            king_x += 1
            king_y += 1

king_x = reverse[king_x]
stone_x = reverse[stone_x]

print(str(king_x) + str(king_y))
print(str(stone_x) + str(stone_y))
