memo = {}
def rec(left, last):
    if left == 0:
        return 1
    if left < 0:
        return 0
    if (left, last) in memo:
        return memo[(left, last)]

    ret = 0
    if last == "bb":
        a = rec(left - 1, "a") # A
        ret += a % 1000000007
    else:
        if left > 1:
            aa = rec(left - 2, "aa")
            ret += aa % 1000000007
    if left > 1:
        b = rec(left - 2, "bb") # BB
        ret += b % 1000000007


    memo[(left, last)] = ret % 1000000007
    return ret % 1000000007

print(rec(int(input()), "bb"))