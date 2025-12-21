bage, bret, bsave, aage, asave = map(int, input().split())
bend = (bret - bage) * bsave
ayears = -(-(bend + 1) // asave)
print(ayears + aage)