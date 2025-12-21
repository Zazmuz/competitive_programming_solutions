cols = int(input())
rows = int(input())

ans = input().split()
scores = [0] * cols
for i in range(rows):
    add = [int(x) for x in input().split()]
    for j in range(cols):
        scores[j] += add[j]

best_index = scores.index(max(scores))
print(ans[best_index])