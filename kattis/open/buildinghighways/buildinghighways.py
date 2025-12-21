input()
costs = [int(_) for _ in input().split()]
print(min(costs) * (len(costs)-1) + sum(costs) - min(costs))