import collections

nei = collections.defaultdict(list)
speeds = collections.defaultdict(float)
ppls = []

for _ in range(int(input())):
    name, spd, superior = input().split()
    spd = float(spd)

    speeds[name] = spd
    ppls.append(name)

    nei[superior].append(name)

root = nei["CEO"][0]

dp_free = {}
dp_paired = {}

def dp(u):
    children = nei[u]

    if not children:return (0, 0), (0, 0)

    s_cnt = 0
    s_spd = 0

    child_res = []

    for v in children:
        res_free, res_paired = dp(v)

        best_v = max(res_paired, res_free)

        s_cnt += best_v[0]
        s_spd += best_v[1]
        child_res.append((best_v, res_free, v))

    dp_free_u = (s_cnt, s_spd)


    best_paired_u = (-1, -1)

    for best_v, res_free_v, v_name in child_res:
        current_count = s_cnt - best_v[0]
        current_speed = s_spd - best_v[1]

        current_count += res_free_v[0]
        current_speed += res_free_v[1]

        current_count += 1
        current_speed += min(speeds[u], speeds[v_name])

        candidate = (current_count, current_speed)

        best_paired_u = max(best_paired_u, candidate)

    return dp_free_u, best_paired_u

final_free, final_paired = dp(root)

ans = max(final_free, final_paired)

print(ans[0], ans[1] / ans[0])