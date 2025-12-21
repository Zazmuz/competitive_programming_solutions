starts_per_rank = [-1] + [5] * 10 + [4] * 5 + [3] * 5 + [2] * 5

current_stars = 0
current_rank = 25
conseq_wins = 0
legend = False
for WL in input():
    if WL == "W":
        conseq_wins += 1
        if conseq_wins >= 3 and current_rank >= 6:
            current_stars += 1
        current_stars += 1

        if current_stars > starts_per_rank[current_rank]:
            current_stars -= starts_per_rank[current_rank]
            current_rank -= 1
            if current_rank <= 0:
                legend = True
                print("Legend")
                exit()
    else:
        conseq_wins = 0
        if current_rank <= 20:
            current_stars -= 1
            if current_stars < 0:
                if current_rank >= 20:
                    current_stars = 0
                    current_rank = 20
                else:
                    current_rank += 1
                    current_stars = starts_per_rank[current_rank] - 1


if legend:
    print("Legend")
else:
    print(current_rank)