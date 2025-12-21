w, h = [int(i) for i in input().split()]
down = []
up = []
up_bool = False
for hh in range(w):
    if not up_bool:
        down.append(int(input()))
    else:
        up.append(h-int(input()))#+0.1)
    up_bool = not up_bool
down.sort()
up.sort()

#print(down)
#print(up)

from bisect import bisect_right

score_each = {}
for height in range(0, h):
    height += 0.5
    #print(height)
    hit = bisect_right(up, height) + len(down) - bisect_right(down, height)
    #if hit == 7:
        #print(height)
    if hit not in score_each:
        score_each[hit] = 0
    score_each[hit] += 1

#print(score_each)
# find smallest key in score_each
sk = min(score_each.keys())
print(sk, score_each[sk])
#print(*[bisect_right(up, i) for i in range(h)])
#print(*[len(down)-bisect_right(down, i) for i in range(h)])