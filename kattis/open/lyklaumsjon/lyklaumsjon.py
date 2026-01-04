import string

n = int(input())

GOOD_acting_user, GOOD_command = '', ''
def is_good():
    if GOOD_command not in commands:
        print('FORBIDDEN')
        return False

    good = False
    for tokens in users[GOOD_acting_user]:
        if tokens not in keys:
            continue
        if GOOD_command in keys[tokens]:
            good = True

    if good:
        print('ACCEPTED')
        return True
    else:
        print('FORBIDDEN')
        return False

def add_user(user):
    global commands, users, keys

    if user in users:
        return 'INVALID'
    if len(user) == 0 or len(user) > 16:
        return 'INVALID'
    for c in user:
        if c not in string.ascii_letters:
            return 'INVALID'

    if is_good(): users[user] = set()

def add_key(key):
    global commands, users, keys

    if key in keys:
        return 'INVALID'
    if len(key) == 0 or len(key) > 10:
        return 'INVALID'
    for c in key:
        if c not in string.ascii_uppercase:
            return 'INVALID'

    if is_good(): keys[key] = set()

def add_command(command, args):
    global commands, users, keys

    if command in commands:
        return 'INVALID'
    if args not in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
        return 'INVALID'
    if len(command) == 0 or len(command) > 20:
        return 'INVALID'

    if is_good(): commands[command] = (int(args), None)

def link_key(key, cmd_user, mode):
    global commands, users, keys

    if key not in keys:
        return 'INVALID'

    if mode == 'USER':
        if cmd_user not in users:
            return 'INVALID'
        if key in users[cmd_user]:
            return 'INVALID'
        if is_good(): users[cmd_user].add(key)
    elif mode == 'COMMAND':
        if cmd_user not in commands:
            return 'INVALID'
        if cmd_user in keys[key]:
            return 'INVALID'
        if is_good(): keys[key].add(cmd_user)
    else:
        return 'INVALID'

def delete_user(user):
    global commands, users, keys

    if user not in users:
        return 'INVALID'

    if is_good():
        users.pop(user)

def delete_key(key):
    global commands, users, keys

    if key not in keys:
        return 'INVALID'

    if is_good(): keys.pop(key)


def delete_command(command):
    global commands, users, keys

    if command not in commands:
        return 'INVALID'

    if is_good():
        commands.pop(command)
        # Remove command from all key links
        for key in keys:
            keys[key].discard(command)

def unlink_key(key, cmd_user, mode):
    global commands, users, keys

    if key not in keys:
        return 'INVALID'

    if mode == 'USER':
        if cmd_user not in users:
            return 'INVALID'
        if key not in users[cmd_user]:
            return 'INVALID'
        if is_good(): users[cmd_user].remove(key)
    elif mode == 'COMMAND':
        if cmd_user not in commands:
            return 'INVALID'
        if cmd_user not in keys[key]:
            return 'INVALID'
        if is_good(): keys[key].remove(cmd_user)
    else:
        return 'INVALID'


commands = {
    'addUser': (1, add_user),
    'addKey': (1, add_key),
    'addCommand': (2, add_command),
    'linkKey': (3, link_key),
    'deleteUser': (1, delete_user),
    'deleteKey': (1, delete_key),
    'deleteCommand': (1, delete_command),
    'unlinkKey': (3, unlink_key),
}

users = {
    'ADMIN': {'ADMINKEY'},
}

keys = {
    'ADMINKEY': set(commands.keys())
}

for _ in range(n):
    parts = input().split()
    if len(parts) < 2:
        print('INVALID')
        continue
    user, cmd, *args = parts
    GOOD_acting_user, GOOD_command = user, cmd

    if cmd not in commands:
        print('INVALID')
        continue
    if user not in users:
        print('INVALID')
        continue

    arg_len, cmd_fn = commands[cmd]
    if arg_len != len(args):
        print('INVALID')
        continue

    if cmd_fn is None:
        is_good()
    else:
        ret = cmd_fn(*args)
        if isinstance(ret, str):
            print(ret)
