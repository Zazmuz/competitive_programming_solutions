n, ppl = map(int, input().split())
correct = input().split()
for _ in range(ppl):
    name = input()
    g = input().split()
    score = sum(1 for i in range(n) if g[i] == correct[i]) / len(correct)
    score *= 10
    score = ((score * 2 + 0.5) // 1) / 2
    print(f"{name}: {score}")