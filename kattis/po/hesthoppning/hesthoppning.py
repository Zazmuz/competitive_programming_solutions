from collections import deque

# Initializing a queue
q = deque()

non_allow = set()

rows, cols = [int(i) for i in input().split()]
start = None
end = None

grid = []
inside_grid = set()
for take_row_input in range(rows):
    grid.append(input())

for find_row in range(rows):
    for find_col in range(cols):
        inside_grid.add((find_row, find_col))
        if grid[find_row][find_col] != '.':
            pos = (find_row, find_col)
            if grid[find_row][find_col] == 'H':
                if start is None:
                    start = pos
                    non_allow.add(pos)
                else:
                    end = pos
            else:
                non_allow.add(pos)


offsets = [(2,1), (-2, 1), (2,-1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
def queue_em(pos):
    for offset in offsets:
        diffed = (pos[0] + offset[0], pos[1] + offset[1])
        if diffed in inside_grid:
            if diffed not in non_allow:
                q.append(diffed)
                non_allow.add(diffed)

queue_em(start)

while q:
    if q[0] == end:
        print('JA')
        exit()
    else:
        queue_em(q[0])
        q.popleft()
print('NEJ')