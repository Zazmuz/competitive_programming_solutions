import sys
def compute_percentage(k, n):
    if k == 0:
        return 100.0
    prev = [1] * (k + 1)
    for i in range(2, n + 1):
        current = [0] * (k + 1)
        for d in range(k + 1):
            total = 0
            for delta in (-1, 0, 1):
                prev_d = d + delta
                if 0 <= prev_d <= k:
                    total += prev[prev_d]
            current[d] = total
        prev = current
    total = sum(prev)
    total_words = (k + 1) ** n
    return (total / total_words) * 100

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    k, n = map(int, line.split())
    percentage = compute_percentage(k, n)
    print(percentage)