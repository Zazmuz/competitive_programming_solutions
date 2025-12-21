print("Gnomes:")
for i in range(int(input())):
    s = [int(_) for _ in input().split()]
    ss = list(sorted(s))
    rss = list(sorted(s, reverse=True))
    print("Ordered" if s == rss or s== ss else "Unordered")