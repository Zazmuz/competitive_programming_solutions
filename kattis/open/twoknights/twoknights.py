from collections import deque
# dont forget to check that they are not on the same square
keys = [
    [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ['^', '^', ' ', ' ', ' ', ' ', ' ', ' ', '^', '^']
    ], [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
        ['^', '^', ' ', ' ', ' ', ' ', ' ', ' ', '^', '^']
    ]
]
# try each state of knightpos + letter state, max 10 cases, 10*100*((10*4)**2) = 1_600_000
k0_s = (0, 3)
k1_s = (9, 3)
start = (k0_s, k1_s, 0)


def inBounds(coords):
    return 0 <= coords[0] < 10 and 0 <= coords[1] < 4


def anyOnShift(coords0, coords1):
    return True if keys[coords0[1]][coords0[0]] == '^' or keys[coords1[1]][coords1[0]] == '^' else False


def isOnShift(coords, who):
    return True if keys[who][coords[1]][coords[0]] == '^' else False

def handle_move(current, move, other, _letter, shift):
    next_pos = (current[0] + move[0], current[1] + move[1])
    if not inBounds(next_pos) or other == next_pos:
        return current, _letter

    if isOnShift(next_pos, shift):
        q.append((next_pos, other, _letter))
        return next_pos, _letter

    letterLandedOn = keys[isOnShift(other, 1 - shift)][next_pos[1]][next_pos[0]]
    if letterLandedOn == word_to_type[_letter]:
        q.append((next_pos, other, _letter + 1))
        return next_pos, _letter + 1

    return current, _letter


k_moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))

while True:
    word_to_type = input()
    if word_to_type == '*':
        break

    # depth, y0, x0, y1, x1
    visited = [[[[[False] * 10 for _ in range(4)] for _ in range(10)] for _ in range(4)] for _ in range(101)]

    q = deque([start])
    while q:
        k0, k1, letter = q.popleft()
        if letter == len(word_to_type):
            print('1')
            break

        if visited[letter][k0[1]][k0[0]][k1[1]][k1[0]]: continue

        visited[letter][k0[1]][k0[0]][k1[1]][k1[0]] = True

        for move in k_moves:
            handle_move(k0, move, k1, letter, 0)
            handle_move(k1, move, k0, letter, 1)
    else:
        print('0')
