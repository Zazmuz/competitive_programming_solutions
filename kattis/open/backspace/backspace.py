toedit = input()

message = []

for i in toedit:
    if i == "<":
        message.pop()
    else:
        message.append(i)
print("".join(message))