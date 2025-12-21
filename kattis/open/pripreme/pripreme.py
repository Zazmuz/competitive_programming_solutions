n = int(input())
times = [int(x) for x in input().split()]
print(max(sum(times), 2 * max(times)))