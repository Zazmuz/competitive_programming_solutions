x, y = map(int, input().split())
r = int(input())

squares = [(x - r, y - r), (x + r, y - r), (x + r, y + r), (x - r, y + r)]
for square in squares:
    print(square[0], square[1])