rows, cols = [int(x) for x in input().split()]
cuts = rows*cols - 1
if cuts % 2 == 1: print("Alf")
else: print("Beata")