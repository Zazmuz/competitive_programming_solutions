import math
def compute_angles(polygon):
    n = len(polygon)
    angles = []
    for i in range(n):
        prev = polygon[(i - 1) % n]
        current = polygon[i]
        next_p = polygon[(i + 1) % n]

        vec_prev = (prev[0] - current[0], prev[1] - current[1])
        vec_next = (next_p[0] - current[0], next_p[1] - current[1])

        dot = vec_prev[0] * vec_next[0] + vec_prev[1] * vec_next[1]

        mag_prev = math.hypot(vec_prev[0], vec_prev[1])
        mag_next = math.hypot(vec_next[0], vec_next[1])

        if mag_prev == 0 or mag_next == 0:
            angles.append(0.0)
            continue

        cos_theta = dot / (mag_prev * mag_next)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_rad = math.acos(cos_theta)

        angles.append(math.degrees(angle_rad))
    return angles


def process_polygon(current):
    while True:
        n = len(current)
        if n <= 3:
            return current
        angles = compute_angles(current)
        min_angle = min(angles)
        min_index = angles.index(min_angle)

        new_poly = current[:min_index] + current[min_index + 1:]

        new_angles = compute_angles(new_poly)
        new_min_angle = min(new_angles)
        if new_min_angle < min_angle:
            return current
        else:
            current = new_poly


while True:
    line = input()
    if line == "0": break
    line = [int(x) for x in line.split()]
    n, rest = line[0], line[1:]
    polygon = []
    for i in range(n):
        polygon.append((rest[i * 2], rest[i * 2 + 1]))

    result = process_polygon(polygon)
    out = []
    out.append(len(result))
    for (x, y) in result:
        out.append(x)
        out.append(y)
    print(" ".join(map(str, out)))