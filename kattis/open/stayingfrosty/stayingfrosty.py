blocks, potions = map(int, input().split())
blocks_trav = potions * 180 * 2
print("YES" if blocks <= blocks_trav else "NO")