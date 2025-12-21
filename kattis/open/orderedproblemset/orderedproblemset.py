n = int(input())
diffs = [int(input()) for _ in range(n)]
aok = False
for k in range(n-1, 0, -1):
    if n % k == 0:
        m_M = []
        for sec in range(0, n, k):
            min = 100
            max = 0
            for i in range(sec, sec + k):
                if diffs[i] < min:
                    min = diffs[i]
                if diffs[i] > max:
                    max = diffs[i]
            m_M.append((min, max))
        ok = True
        for i in range(len(m_M) - 1):
            if m_M[i][1] > m_M[i + 1][0] or m_M[i + 1][1] < m_M[i][0]:
                ok = False
                break
        if ok:
            print(n // k)
            aok = True
if not aok:
    print(-1)