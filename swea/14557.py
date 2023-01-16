def check(deck):
    deck_new = deck
    if len(deck) > 3:
        if deck[0] == 1:
            if deck[1] == 0:
                if deck[2] == 0:
                    if 1 in deck[1:]:
                        return 'no'

        if deck[-1] == 1:
            if deck[-2] == 0:
                if deck[-3] == 0:
                    if 1 in deck[:-1]:
                        return 'no'

    elif len(deck) == 3:
        if deck.count('1') == 1:
            return 'yes'

        elif deck.count('1') == 3:
            return 'yes'

        else:
            return 'no'

    if deck[0] == '1':
        deck_new.remove(deck[0])
        deck_new = change(deck, 0)
        check(deck_new)

    else:
        deck_new.remove(deck[0])
        check(deck_new)

    return check(deck_new)


def change(deck_change, index):
    if deck_change[index] == '1':
        deck_change[index] = '0'

    elif deck_change[index] == '0':
        deck_change[index] = '1'

    return deck_change


ip = int(input())

for i in range(1, ip + 1):
    deck = input()
    ans = check(list(deck))
    print("#%d %s" % (i, ans))
