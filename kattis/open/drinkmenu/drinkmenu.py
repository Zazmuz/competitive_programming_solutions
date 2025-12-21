from collections import defaultdict
drinks, people = map(int, input().split())
drink_names = [input() for _ in range(drinks)]
ppl_counter = defaultdict(int)
for _ in range(people):
    name = input()
    print(drink_names[ppl_counter[name]])
    ppl_counter[name] += 1