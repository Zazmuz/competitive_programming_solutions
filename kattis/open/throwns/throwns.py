students, m = map(int, input().split())
throws = []

pos = 0

commands = iter(input().split())
nxt = lambda: next(commands, None)
while (command := nxt()) is not None:
    if command == 'undo':
        for undo in range(int(nxt())):
            throws.pop()
    else:
        throws.append(int(command))

for p in throws:
    pos += p
    pos %= students
print(pos)