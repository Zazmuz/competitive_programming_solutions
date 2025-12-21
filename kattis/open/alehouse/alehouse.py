ppl, stay_time = map(int, input().split())

actions = []
for _ in range(ppl):
    come, leave = map(int, input().split())
    actions.append((max(come - stay_time, 0), 1, _))
    actions.append((leave, 2, _))
actions.sort()

from collections import deque
current_queue = deque()

max_amnt = 0
current = set()
for action in actions:
    if action[1] == 1:
        current.add(action[2])
    else:
        current.remove(action[2])
    max_amnt = max(max_amnt, len(current))
print(max_amnt)


# |         |
#   |     |
#  |       |
#   |   |
# |                 |

