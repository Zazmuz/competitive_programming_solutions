sum1 = sum(int(_) for _ in input().split())
sum2 = sum(int(_) for _ in input().split())

if sum1 < sum2:
    print("Emma")
elif sum1 > sum2:
    print("Gunnar")
else:
    print("Tie")