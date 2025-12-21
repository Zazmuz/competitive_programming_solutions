grid = []
for _ in range(2):
    for i in input():
        grid.append(i)

visited = set()
from collections import deque
q = [(grid, 0)]
q = deque(q)
while q:
    state, steps = q.popleft()
    if tuple(state) in visited:
        continue
    swap_pos = state.index('-')
    visited.add(tuple(state))
    if state == ['1', '2', '3', '-']:
        print(steps)
        exit()
    if swap_pos % 2 == 0:
        new_state1 = state[:]
        new_state1[swap_pos], new_state1[swap_pos + 1] = new_state1[swap_pos + 1], new_state1[swap_pos]
        q.append((new_state1, steps + 1))
        new_state2 = state[:]
        new_state2[swap_pos], new_state2[(swap_pos + 2) % 4] = new_state2[(swap_pos + 2) % 4], new_state2[swap_pos]
        q.append((new_state2, steps + 1))
    else:
        new_state1 = state[:]
        new_state1[swap_pos], new_state1[swap_pos - 1] = new_state1[swap_pos - 1], new_state1[swap_pos]
        q.append((new_state1, steps + 1))
        new_state2 = state[:]
        new_state2[swap_pos], new_state2[(swap_pos + 2) % 4] = new_state2[(swap_pos + 2) % 4], new_state2[swap_pos]
        q.append((new_state2, steps + 1))
print(-1)