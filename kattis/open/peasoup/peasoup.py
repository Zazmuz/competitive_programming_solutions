for _ in range(int(input())):
    items = int(input())
    name = input()
    want = {'pancakes', 'pea soup'}
    got = set()
    for _ in range(items):
        got.add(input())
    if not want-got:
        print(name)
        exit()
print('Anywhere is fine I guess')