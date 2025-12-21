streets, drivers = map(int, input().split())
sl = {}
for i in range(streets):
    sl[input()] = i

for driver in range(drivers):
    s, e = input().split()
    print(abs(sl[s] - sl[e])-1)