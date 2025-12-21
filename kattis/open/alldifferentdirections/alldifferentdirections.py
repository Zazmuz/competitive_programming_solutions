import math
def solve_instructions(pos, angle, instr):
    x, y = pos
    for i in instr:
        if i[0] == 'walk':
            x += float(i[1]) * math.cos(math.radians(angle))
            y += float(i[1]) * math.sin(math.radians(angle))
        elif i[0] == 'turn':
            angle += float(i[1])

    return x, y

while True:
    n = int(input())
    if n == 0:
        break
    exesandwhys = []

    for _ in range(n):
        line = input().split()
        x, y = float(line[0]), float(line[1])
        angle = float(line[3])
        instructions = line[4:]
        instructions = [(instructions[i], instructions[i+1]) for i in range(0, len(instructions), 2)]
        x, y = solve_instructions((x, y), angle, instructions)
        exesandwhys.append((x, y))

    x = sum([x for x, y in exesandwhys]) / n
    y = sum([y for x, y in exesandwhys]) / n
    biggest = max([math.hypot(x - x0, y - y0) for x0, y0 in exesandwhys])
    print(x, y, biggest)