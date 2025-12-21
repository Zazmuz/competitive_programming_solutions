from math import log10, floor
def findDigits(n, b):
    if (n < 0):
        return 0

    M_PI = 3.141592
    M_E = 2.7182
    if (n <= 1):
        return 1

    x = ((n * log10(n / M_E) + log10(2 * M_PI * n) / 2.0)) / (log10(b))

    return floor(x) + 1

import sys
for line in sys.stdin.readlines():
    print(findDigits(int(line), 10))