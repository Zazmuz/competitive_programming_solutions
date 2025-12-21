from math import ceil
rank_to_score = {   1: 100,
                    2: 75,
                    3: 60,
                    4: 50,
                    5: 45,
                    6: 40,
                    7: 36,
                    8: 32,
                    9: 29,
                    10: 26,
                    11: 24,
                    12: 22,
                    13: 20,
                    14: 18,
                    15: 16,
                    16: 15,
                    17: 14,
                    18: 13,
                    19: 12,
                    20: 11,
                    21: 10,
                    22: 9,
                    23: 8,
                    24: 7,
                    25: 6,
                    26: 5,
                    27: 4,
                    28: 3,
                    29: 2,
                    30: 1}
# if tie, as many as tie downwards average
# if onsite +1
# if not participate 0

# ;; sorted by ;;
# problems solved, decending
# time penalty, ascending
# last submission time, ascending

# if all 3 sorted by equal, then tie


    # input::
# n :contestants
#   n_lines
# s, p, f, o :AC_problems, penalty, lastSubmissionTime, onSitePoints

n = int(input())

ppl = [[int(_) for _ in line.split()] for line in [input() + " "+str(i) for i in range(n)]]

ppl.sort(key=lambda x: (-x[0], x[1], x[2]))

current = None
sames = 0
rank_rn = 0
scores = []
other_info = []
#print(ppl)
ppl.append([None, None, None, None, None])
for person in ppl:
    if not current:
        current = person
        sames = 1
        other_info.append((person[3], person[4]))
        continue
    if current[:3] == person[:3]:
        sames += 1
        other_info.append((person[3], person[4]))
    else:
        to_score = []
        for i in range(sames):
            rank_rn += 1
            if rank_rn > 30:
                to_score.append(0)
            else:
                to_score.append(rank_to_score[rank_rn])
        score_to_give = ceil(sum(to_score) / sames)
        for i in range(sames):
            scores.append((other_info[i][1], score_to_give + other_info[i][0]))
        current = person
        other_info = [(person[3], person[4])]
        sames = 1

#print(scores)
scores.sort(key=lambda x: x[0])
for score in scores:
    print(score[1])