a, b = map(int, input().split())
d = abs(a-b)
s = 's' if d != 1 else ''
if a-b > 0:
    print(f"Dr. Chaz needs {d} more piece{s} of chicken!")
else:
    print(f"Dr. Chaz will have {d} piece{s} of chicken left over!")