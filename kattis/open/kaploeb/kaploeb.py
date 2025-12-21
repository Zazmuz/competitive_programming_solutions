recorded_laps, needed_for_race, start_numbers_handed_out = map(int, input().split())
person_time_laps = {}
in_race = set()
for i in range(recorded_laps):
    person, time = input().split()
    time_min, time_sec = map(int, time.split('.'))
    person = int(person)
    in_race.add(person)
    tot_time = time_min * 60 + time_sec
    if person not in person_time_laps:
        person_time_laps[person] = (tot_time, 1)
    else:
        person_time_laps[person] = (person_time_laps[person][0] + tot_time, person_time_laps[person][1] + 1)

to_sort = []
for i in in_race:
    a, b = person_time_laps[i]

    if b < needed_for_race:
        continue
    to_sort.append((a, i))
to_sort.sort()
for i in to_sort:
    print(i[1])