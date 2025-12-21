from sys import setrecursionlimit
setrecursionlimit(10**6)
word_amount = int(input())
words = []

for _ in range(word_amount):
    words.append(input())

add_list = [[] for _ in range(word_amount)]
start = set([i for i in range(word_amount)])
for i in range(word_amount - 1):
    add_to, add_from = [int(x) for x in input().split()]
    add_list[add_to-1].append(add_from-1)
    start.discard(add_from-1)
start = list(start)[0]
def dfs(i):
    if not add_list[i]:
        print(words[i], end="")
    else:
        print(words[i], end="")
        for j in add_list[i]:
            dfs(j)
dfs(start)