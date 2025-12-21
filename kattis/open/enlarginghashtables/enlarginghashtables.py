def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    while not is_prime(n):
        n += 2
    return n

while True:
    n = int(input())
    if n == 0:
        break

    if is_prime(n):
        print(next_prime(2*n))
    else:
        print(next_prime(2*n), f"({n} is not prime)")