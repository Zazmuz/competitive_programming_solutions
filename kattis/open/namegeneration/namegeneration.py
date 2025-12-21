p = 'aeiou'
q = [i+j for i in p for j in p]
l = ["x".join((a, b, c, d)) for a in q for b in q for c in q for d in q]
print("\n".join(l[i] for i in range(int(input()))))
