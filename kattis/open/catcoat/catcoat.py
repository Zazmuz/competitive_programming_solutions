from collections import defaultdict

genes_from_color = {
    "Black": "B-D-oo",
    "Blue": "B-ddoo",
    "Chocolate": "bbD-oo",
    "Lilac": "bbddoo",
    "Red": "--D-OO",
    "Cream": "--ddOO",
    "Black-Red Tortie": "B-D-Oo",
    "Blue-Cream Tortie": "B-ddOo",
    "Chocolate-Red Tortie": "bbD-Oo",
    "Lilac-Cream Tortie": "bbddOo",
}


def wild(s):
    v = [""]
    for i, ch in enumerate(s):
        if ch == '-':
            base = 'b' if i < 2 else 'd' if i < 4 else 'o'  # find base letter

            for j in range(len(v)):
                v.append(v[j] + base.upper())
                v[j] = v[j] + base
        else:
            for idx in range(len(v)):
                v[idx] += ch
    return v


class Cat:
    def __init__(self, is_female, dom_b, dom_d, dom_o):
        self.is_female = is_female
        self.dom_b = dom_b
        self.dom_d = dom_d
        self.dom_o = dom_o

    def parse(s):
        dom_b = 0
        dom_d = 0
        dom_o = 0
        if len(s) == 6:
            is_female = True
            if s[5] == 'O':
                dom_o += 1
        else:
            is_female = False
        if s[4] == 'O':
            dom_o += 1
        if s[0] == 'B':
            dom_b += 1
        if s[1] == 'B':
            dom_b += 1
        if s[2] == 'D':
            dom_d += 1
        if s[3] == 'D':
            dom_d += 1
        return Cat(is_female, dom_b, dom_d, dom_o)

    def get_color(self):
        if self.dom_o == 0:
            if self.dom_b >= 1 and self.dom_d >= 1:
                return "Black"

            elif self.dom_b >= 1 and self.dom_d == 0:
                return "Blue"

            elif self.dom_b == 0 and self.dom_d >= 1:
                return "Chocolate"

            elif self.dom_b == 0 and self.dom_d == 0:
                return "Lilac"

        elif (self.dom_o == 2 and self.is_female) or (self.dom_o == 1 and not self.is_female):
            if self.dom_d >= 1:
                return "Red"

            elif self.dom_d == 0:
                return "Cream"

        elif self.is_female and self.dom_o == 1:
            if self.dom_b >= 1:
                if self.dom_d >= 1:
                    return "Black-Red Tortie"

                elif self.dom_d == 0:
                    return "Blue-Cream Tortie"

            if self.dom_b == 0:
                if self.dom_d >= 1:
                    return "Chocolate-Red Tortie"

                elif self.dom_d == 0:
                    return "Lilac-Cream Tortie"

    def stringify(self):
        s = ""

        for i in range(2):
            s += 'B' if i < self.dom_b else 'b'

        for i in range(2):
            s += 'D' if i < self.dom_d else 'd'

        if self.is_female:
            for i in range(2):
                s += 'O' if i < self.dom_o else 'o'
        else:
            s += 'O' if self.dom_o > 0 else 'o'

        s += " (female)" if self.is_female else " (male)"
        return s

    def breed(self, other):
        female = self if self.is_female else other
        male = other if not other.is_female else self
        children = []

        for g1f in range(2):  # g1f, g1m for B-locus
            for g1m in range(2):
                for g2f in range(2):  # g2f, g2m for D-locus
                    for g2m in range(2):
                        for g3f in range(2):  # g3f for O-locus from female.
                            for gender in range(2):
                                is_female_child = gender == 0

                                dom_b = 0
                                dom_d = 0
                                dom_o = 0

                                if g1f < female.dom_b:
                                    dom_b += 1

                                if g1m < male.dom_b:
                                    dom_b += 1

                                if g2f < female.dom_d:
                                    dom_d += 1

                                if g2m < male.dom_d:
                                    dom_d += 1

                                if g3f < female.dom_o:
                                    dom_o += 1

                                if is_female_child and male.dom_o > 0:
                                    dom_o += 1

                                children.append(Cat(is_female_child, dom_b, dom_d, dom_o))
        return children


f_color = input()
m_color = input()

males = []
females = []
for s in wild(genes_from_color[m_color]):
    males.append(Cat.parse(s[:-1]))

for s in wild(genes_from_color[f_color]):
    females.append(Cat.parse(s))

c = defaultdict(int)
tot = 0

for m in males:
    for f in females:
        children = m.breed(f)
        for child in children:
            col = child.get_color()
            c[col] += 1
            tot += 1

result = sorted(((color, cnt) for color, cnt in c.items()), key=lambda x: (-x[1], x[0]))
for color, cnt in result:
    prob = cnt / tot
    print(f"{color} {prob:.9f}")
