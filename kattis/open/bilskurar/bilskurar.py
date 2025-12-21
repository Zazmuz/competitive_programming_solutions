n = int(input())
froms = [int(_) for _ in input().split()]
tos = [int(_) for _ in input().split()]
to_to_from = {tos[i]:i for i in range(n)}

for i in range(n):
    froms[i] = to_to_from[froms[i]]


def count_inversions_merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = count_inversions_merge_sort(arr[:mid])
    right, right_inv = count_inversions_merge_sort(arr[mid:])
    merged = []
    i = j = inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, left_inv + right_inv + inv

print(count_inversions_merge_sort(froms)[1])