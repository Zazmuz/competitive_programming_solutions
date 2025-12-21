papers, pile_amount = map(int, input().split())

piles = []
for pile in range(pile_amount):
    pile_size, *pile_content = map(int, input().split())
    piles.append(pile_content)



for movement in range(int(input())):
    froms, tos, amounts = map(int, input().split())
    pile = []
    for move in range(amounts):
        paper = piles[froms-1].pop()
        pile.append(paper)
    pile.reverse()
    piles[tos-1].extend(pile)

for pile in piles:
    print(*pile)