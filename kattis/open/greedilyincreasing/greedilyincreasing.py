s = 0
n = input()
added = []
nums = [int(i) for i in input().split()]
b = 0
for num in nums:
    if num > b:
        s += num
        added.append(num)
        b = num
print(s)
print(*added)