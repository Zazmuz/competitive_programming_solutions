n, m = [int(x) for x in input().split()]
n += 2
print('Arnar' if m <n - n//3 else 'Unnar')