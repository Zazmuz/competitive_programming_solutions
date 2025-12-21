n, k = map(int, input().split())
MOD = 10**9 + 7

points_needed = k + 2

values = []
acc = 0
for i in range(points_needed):
    acc = (acc + pow(i+1, k, MOD)) % (MOD)
    values.append(acc)

n_mod = n % MOD

fact = [1] * (points_needed + 1)
for i in range(1, points_needed + 1):
    fact[i] = fact[i - 1] * i % (MOD)

invfact = [1] * (points_needed + 1)
invfact[points_needed] = pow(fact[points_needed], MOD - 2, MOD)

for i in range(points_needed, 0, -1):
    invfact[i - 1] = invfact[i] * i % (MOD)

# pre = prod, 1 to i
pre = [1] * (points_needed + 2)
for i in range(1, points_needed + 1):
    pre[i] = pre[i - 1] * (n_mod - i) % (MOD)

# suf = prod, i to points_needed
suf = [1] * (points_needed + 3)
for i in range(points_needed, 0, -1):
    suf[i] = suf[i + 1] * (n_mod - i) % (MOD)

# lagrange interpolation
ans = 0
for i in range(1, points_needed + 1):
    num = pre[i - 1] * suf[i + 1] % MOD

    den = (fact[i - 1] * fact[points_needed - i]) % MOD
    term = values[i-1] * num % MOD
    term = term * pow(den, MOD - 2, MOD) % MOD

    if (points_needed - i) % 2 == 1:
        term = (MOD - term) % MOD

    ans = (ans + term) % MOD

print(ans % MOD)