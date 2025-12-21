f = int(input())
me = input()
friend = input()

fw = len(friend) - f
d = sum(me[i] != friend[i] for i in range(len(me)))
if d <= fw:
    print(f + d)
else:
    print(len(friend) - abs(d - fw))