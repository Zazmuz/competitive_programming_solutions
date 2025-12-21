import random
c = {
    0: "abcdefghijklmnopqrstuvwxyz",
    1: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    2: "0123456789",
    3: "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
}

def generate_passwords():
    used = [random.randint(2, 3) for _ in range(4)]

    while sum(used) < 8:
        used[random.randint(0, 3)] += 1

    while sum(used) > 12:
        used[random.randint(0, 3)] -= 1

    length = sum(used)

    password = ['']* length
    for _ in range(length):
        to_use = random.randint(0, 3)
        while used[to_use] == 0:
            to_use = random.randint(0, 3)

        password[_] = random.choice(c[to_use])
        used[to_use] -= 1
    random.shuffle(password)

    return ''.join(password)

for _ in range(int(input())):
    print(generate_passwords())