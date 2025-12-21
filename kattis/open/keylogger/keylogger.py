new = """clank
bong
click
tap
poing
clonk
clack
ping
tip
cloing
tic
cling
bing
pong
clang
pang
clong
tac
boing
boink
cloink
rattle
clock
toc
clink
tuc
whack
""".split("\n")
conv_small = {news : old for old, news in zip("abcdefghijklmnopqrstuvwxyz ", new)}
conv_big = {news : old for old, news in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", new)}


shift = False
caps = False
stack = []
for c in range(int(input())):
    sound = input()
    if sound == "bump":
        caps = not caps
    elif sound == "dink":
        shift = True
    elif sound == "thumb":
        shift = False
    elif sound == "pop":
        if len(stack) != 0:
            stack.pop(-1)
    else:
        if (shift+caps) % 2 == 0:
            stack.append(conv_small[sound])
        else:
            stack.append(conv_big[sound])

print("".join(stack))