n, m, q = map(int, input().split())
who = [input() for _ in range(n)]
traits = []
for qq in range(q):
    a, b = input().split()
    a = int(a) - 1
    traits.append((a, b))

ppl = 0
ppl_p = []
for idx, w in enumerate(who):
    matches = True
    for t in traits:
        spot, val = t
        if w[spot] != val:
            matches = False
            break
    if matches:
        ppl += 1
        ppl_p.append(idx + 1)

if ppl == 1:
    print("unique")
    print(ppl_p[0])
elif ppl > 1:
    print("ambiguous")
    print(len(ppl_p))