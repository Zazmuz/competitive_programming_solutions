w, s = map(int, input().split())
gold = 29370
tungsten = 29260
c = s * (s + 1) // 2
print((w - c * tungsten) // (gold - tungsten))