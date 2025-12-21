a = input()
b = input()
x = a.count('S')
y = b.count('S')
def pa(x, y):
    return x + y
def pm(x, y):
    if y == 0:
        return 0
    return pa(x, pm(x, y - 1))
r = pm(x, y)
result = 'S(' * r + '0' + ')' * r
print(result)