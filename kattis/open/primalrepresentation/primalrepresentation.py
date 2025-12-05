import sys
import subprocess
from collections import Counter

d = sys.stdin.read().split()

a = []
b = []
for x in d:
    if x.startswith('-'):
        b.append(True)
        a.append(x[1:])
    else:
        b.append(False)
        a.append(x)

proc = subprocess.Popen(
    ['factor'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
out, _ = proc.communicate('\n'.join(a))
r = out.strip().split('\n')

m = min(len(r), len(b))

for i in range(m):
    ln = r[i]
    neg = b[i]
    p = ln.split()

    if not p:
        continue

    fs = p[1:]
    cnt = Counter(fs)
    ans = []

    if neg:
        ans.append('-1')

    ks = sorted(cnt.keys(), key=int)
    for k in ks:
        v = cnt[k]
        if v > 1:
            ans.append(f"{k}^{v}")
        else:
            ans.append(k)
    print(*ans)