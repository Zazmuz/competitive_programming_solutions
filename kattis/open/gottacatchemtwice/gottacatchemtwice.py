n = int(input())
s = set()
for _ in range(n):
    name = input()
    s.add(name)
print(len(s)+1)