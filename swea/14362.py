def check(list, robot, l):
    robot_new = robot
    list_new = list
    l_new = l

    if l < ((robot_new[0]) ** 2) + ((robot_new[1]) ** 2):
        l_new = ((robot_new[0])**2) + ((robot_new[1])**2)

    if len(list) == 0:
        return l_new

    else:
        if list[0] == 'S':
            if robot[2] == 'R':
                robot_new[0] += 1
                list_new.remove(list[0])
                check(list_new, robot_new, l_new)

            elif robot[2] == 'U':
                robot_new[1] += 1
                list_new.remove(list[0])
                check(list_new, robot_new, l_new)

            elif robot[2] == 'L':
                robot_new[0] -= 1
                list_new.remove(list[0])
                check(list_new, robot_new, l_new)

            elif robot[2] == 'D':
                robot_new[1] -= 1
                list_new.remove(list[0])
                check(list_new, robot_new, l_new)

        elif list[0] == 'R':
            list_new.remove(list[0])
            if robot[2] == 'R':
                robot_new[2] = 'D'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'U':
                robot_new[2] = 'R'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'L':
                robot_new[2] = 'U'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'D':
                robot_new[2] = 'L'
                check(list_new, robot_new, l_new)

        elif list[0] == 'L':
            list_new.remove(list[0])
            if robot[2] == 'R':
                robot_new[2] = 'U'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'U':
                robot_new[2] = 'L'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'L':
                robot_new[2] = 'D'
                check(list_new, robot_new, l_new)

            elif robot[2] == 'D':
                robot_new[2] = 'R'
                check(list_new, robot_new, l_new)

    return check(list_new, robot_new, l_new)


ip = int(input())

for i in range(1, ip + 1):
    robot = [0, 0, 'R']
    order = list(input())
    ans = check(order, robot, 0)
    print(ans)
    #print("#%d %d" % (i, i))

