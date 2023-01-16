ip = int(input())

for i in range(ip):
    case = list(map(int, input().split()))
    case1 = case[0:2]
    case2 = case[3:5]
    length = (((case[3] - case[0])**2) + ((case[4] - case[1])**2))**(1/2)
    if case1 == case2:
        if case[2] == case[5]:
            print("-1")

        else:
            print("0")

    elif (length == (case[2] + case[5])) or (length == abs(case[5] - case[2])):
        print("1")

    elif length > (case[2] + case[5]):
        print("0")

    elif ((length + case[2]) < case[5]) or ((length + case[5]) < case[2]):
        print("0")


    else:
        print("2")
