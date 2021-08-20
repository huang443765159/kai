moves = ('R', 'R', 'L', 'U', 'D', 'L')


def search_origin(moves_1):
    x = 0
    y = 0
    for i in moves_1:
        if i == "R":
            x += 1
        elif i == 'L':
            x -= 1
        elif i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
    return x == 0 and y == 0


if __name__ == '__main__':

    bingo = search_origin(moves)
    print(bingo)

