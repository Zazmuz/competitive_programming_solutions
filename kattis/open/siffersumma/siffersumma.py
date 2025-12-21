N = [int(c) for c in input()]
n = len(N)

sufsum = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    sufsum[i] = N[i] + sufsum[i + 1]

for i in range(n - 1, -1, -1): # no carry
    if N[i] == 9: continue
    required_sum_after = sufsum[i + 1] - 1
    num_digits = n - i - 1
    if required_sum_after < 0 or required_sum_after > 9 * num_digits:
        continue # impossible without carry

    N[i] += 1
    ending = []
    required_with_current = required_sum_after
    for j in range(num_digits):
        max_after_current = 9 * (num_digits - j - 1)
        d = max(0, required_with_current - max_after_current)
        ending.append(d)
        required_with_current -= d
    print(''.join(map(str, N[:i + 1] + ending)))
    exit()

remaining_sum = sufsum[0] - 1
ending = []
for j in range(n): # yes carry
    max_after_current = 9 * (n - j - 1)
    d = max(0, remaining_sum - max_after_current)
    ending.append(d)
    remaining_sum -= d

print('1' + ''.join(map(str, ending)))