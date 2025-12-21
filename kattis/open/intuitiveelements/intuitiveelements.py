for _ in range(int(input())):
    e = set(input())
    abv = set(input())
    print("YES" if all([c in e for c in abv]) else "NO")