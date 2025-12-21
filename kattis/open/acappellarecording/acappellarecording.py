notes, diff_in_rec = [int(x) for x in input().split()]
to_sing = sorted([int(input()) for x in range(notes)])
new_start_score = 0
next_new_start = -1
for note in to_sing:
    if note > next_new_start:
        new_start_score += 1
        next_new_start = note + diff_in_rec
print(new_start_score)