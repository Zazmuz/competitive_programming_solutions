addr = input()
if "." in addr:
    addr = addr.split(".")[::-1] + ["in-addr.arpa."]
    print(".".join(addr))
else:
    new_addr = addr.split(":")
    while len(new_addr) < 8:
        where = new_addr.index("")
        new_addr.insert(where, "0000")
    for i in range(len(new_addr)):
        new_addr[i] = new_addr[i].zfill(4)
        new_addr[i] = ".".join(new_addr[i][::-1])
    print(".".join(new_addr[::-1]) + ".ip6.arpa.")
