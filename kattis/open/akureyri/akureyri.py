from collections import Counter

cities = Counter()

for i in range(int(input())*2):
    if i % 2 == 0:
        input()
        continue

    city = input()
    cities[city] += 1

for city, count in cities.items():
    print(city, count)