memo = {}
def rec(left):
    if left == 0:
        return 1
    if left < 0:
        return 0

    if left in memo:
        return memo[left]

    ret = 0
    for i in range(1,4):
        ret += rec(left-i)

    memo[left] = ret
    return ret

print(rec(int(input())))