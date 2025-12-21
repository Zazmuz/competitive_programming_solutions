def q(guess):
    print(f"buf[{guess}]")
    ret = input()
    if ret == "Segmentation fault (core dumped)":
        exit()
    return ret == "0"

def binary_search(_lo, _hi):
    lo = _lo
    hi = _hi
    while lo < hi:
        mid = (lo + hi) // 2
        if q(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def ans(ans):
    print(f"strlen(buf) = {ans}")

high = 1
while True:
    low = high
    high = low * 2
    if q(high): # if 0
        ans(binary_search(low, high))
        break