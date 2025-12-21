personal_number = input().strip()
digits = personal_number.replace('-', '')
vals = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

total = sum(int(d) * w for d, w in zip(digits, vals))
print(1 if total % 11 == 0 else 0)