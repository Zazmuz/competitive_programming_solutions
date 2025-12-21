def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

gates = {}
inputs = {}
outputs = []
n = int(input())
for _ in range(n):
    line = input().split()
    TYPE = line[0]
    if TYPE == 'INNTAK':
        name = line[1]
        val = 1 if line[2] == 'SATT' else 0
        inputs[name] = val
        gates[name] = ('src', val)
    elif TYPE == 'UTTAK':
        inp = line[1]
        outputs.append((line[1], inp))
    elif TYPE == 'OG':
        inp1 = line[1]
        inp2 = line[2]
        name = line[3]
        gates[name] = ('and', inp1, inp2)
    elif TYPE == 'EDA':
        inp1 = line[1]
        inp2 = line[2]
        name = line[3]
        gates[name] = ('or', inp1, inp2)
    elif TYPE == 'EKKI':
        inp = line[1]
        name = line[2]
        gates[name] = ('not', inp)

def evaluate(gate):
    if gate not in gates:
        return 0
    g = gates[gate]
    if g[0] == 'src':
        return g[1]
    elif g[0] == 'and':
        return AND(evaluate(g[1]), evaluate(g[2]))
    elif g[0] == 'or':
        return OR(evaluate(g[1]), evaluate(g[2]))
    elif g[0] == 'not':
        return NOT(evaluate(g[1]))
    return 0

for name, inp in outputs:
    val = evaluate(inp)
    print(f"{name} {'SATT' if val else 'OSATT'}")