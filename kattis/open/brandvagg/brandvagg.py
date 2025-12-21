rules = []
for i in range(int(input())):
    rls = input().split()
    dpnd = [g.split("=") for g in rls[1:]]
    rules.append((rls[0], *dpnd))
calls = []
ip_occurrences = {}
for i in range(int(input())):
    ip, port = input().split(":")

    calls.append((ip, port))

for i, data in enumerate(calls):
    ip, port = data
    i += 1
    if ip in ip_occurrences:
        ip_occurrences[ip] += 1
    else:
        ip_occurrences[ip] = 1
    if i > 1000:
        ip_occurrences[calls[i-1001][0]] -= 1
    for rule in rules:
        do = True
        for ats in rule[1:]:
            dt = ats
            if dt[0] == "ip":
                if dt[1] != ip:
                    do = False
            elif dt[0] == "port":
                if dt[1] != port:
                    do = False
            elif dt[0] == "limit":
                if ip_occurrences[ip] < int(dt[1]):
                    do = False
        if do:
            print(rule[0], i)
            if rule[0] == "accept" or rule[0] == "drop":
                break