import itertools

data = [int(x) for x in input().split()]
boxes = data[:-2]
h1, h2 = data[-2], data[-1]
h1h2 = {(h1, h2), (h2, h1)}
total = sum(boxes)
def is_valid(triplet):
    sorted_triplet = sorted(triplet, reverse=True)
    return sorted_triplet[0] > sorted_triplet[1] > sorted_triplet[2]


for combo in itertools.combinations(boxes, 3):
    sum_combo = sum(combo)
    sum_remain = total - sum_combo

    if (sum_combo, sum_remain) not in h1h2: continue # cant be the sum combo

    if sum_combo == h1 and sum_remain == h2:
        first_tower = combo
        second_tower = [x for x in boxes if x not in combo]
    else:
        first_tower = [x for x in boxes if x not in combo]
        second_tower = combo

    if is_valid(first_tower) and is_valid(second_tower):
        first_sorted = sorted(first_tower, reverse=True)
        second_sorted = sorted(second_tower, reverse=True)
        print(' '.join(map(str, first_sorted)) + ' ' + ' '.join(map(str, second_sorted)))
        break