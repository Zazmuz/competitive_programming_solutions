s=0
for i in range(int(input())):
    input()
    s+=int(input())

print("Lagom" if s==0 else "Usch, vinst" if s>0 else "Nekad")