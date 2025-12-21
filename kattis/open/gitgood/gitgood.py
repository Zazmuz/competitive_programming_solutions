path = []
edited = set()
for command in range(int(input())):
    command, file = input().split()
    if command == 'cd':
        if file == '..':
            path.pop()
        else:
            path.append(file)
    else:
        edited.add('/'.join(path + [file]))

for file in sorted(edited):
    print("git add", file)
print("git commit")
print("git push")