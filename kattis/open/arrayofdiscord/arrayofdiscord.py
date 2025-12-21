brrr = int(input())
arr = [int(i) for i in input().split()]


def cringethenum(n, num):
    n = list(str(n))
    if num != "0" or len(n) == 1:
        n[0] = num
    n = int(''.join(n))
    return n


tmp = [_ for _ in arr]
for number_in_array in range(len(arr)):
    for pot_number in "019":
        tmp[number_in_array] = cringethenum(tmp[number_in_array], pot_number)
        if not all(tmp[i] <= tmp[i + 1] for i in range(len(tmp) - 1)):
            print(" ".join([str(_) for _ in tmp]))
            exit(0)
        tmp[number_in_array] = arr[number_in_array]

print("impossible")
