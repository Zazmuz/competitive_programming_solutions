password = input()
class linked_list:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


curr = linked_list('')
start = curr
for c in password:
    if c == 'L':
        curr = curr.prev
    elif c == 'R':
        curr = curr.next
    elif c == 'B':
        curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        curr = curr.prev
    else:
        new = linked_list(c)
        new.next = curr.next
        new.prev = curr
        curr.next = new
        curr = new
        if curr.next:
            curr.next.prev = curr

start = start.next
l = []
while start:
    l.append(start.val)
    start = start.next
print("".join(l))