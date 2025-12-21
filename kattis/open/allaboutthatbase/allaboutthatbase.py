def char_to_val(c):
    if c.isdigit():
        return int(c)
    return 10 + ord(c) - ord('a')
def outside_range(lo, hi, x):
    return x < lo or x > hi
def check_base(num_str, base):
    if outside_range(1, 36, base):
        return False
    if base == 1:
        return all(c == '1' for c in num_str)

    if len(num_str) == 0 or len(num_str) > 1 and num_str[0] == '0':
        return False

    for c in num_str:
        if char_to_val(c) >= base:
            return False
    return True
def to_base10(num_str, base):
    return len(num_str) if base == 1 else int(num_str, base)

inf = (1 << 32) - 1
for _ in range(int(input())):
    a, op, b, _, c = input().split()
    valid_bases = [False] * 37
    for B in range(1, 37):
        if not all(check_base(x, B) for x in (a, b, c)): continue

        a_base, b_base, c_base = map(lambda x: to_base10(x, B), (a, b, c))

        if any(outside_range(1, inf, x) for x in (a_base, b_base, c_base)): continue

        if eval(f"{a_base} {op} {b_base} == {c_base}"):
            valid_bases[B] = True

    if sum(valid_bases):
        out = ''
        for i in range(1, 37):
            if valid_bases[i]:
                out += str(i) if i <= 9 else chr(ord('a') + (i - 10)) if i <= 35 else '0'
        print(out)
    else:
        print("invalid")