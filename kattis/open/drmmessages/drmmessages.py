msg = input()
left = msg[:len(msg)//2]
right = msg[len(msg)//2:]

left_sum = sum(ord(c) - ord('A') for c in left)
right_sum = sum(ord(c) - ord('A') for c in right)
left_sum, right_sum = left_sum % 26, right_sum % 26
new_msg = [chr((ord(c) - ord('A') + left_sum) % 26 + ord('A')) for c in left]
rotations = [chr((ord(c) - ord('A') + right_sum) % 26 + ord('A')) for c in right]

final_msg = [chr((ord(c) - ord('A') + ord(rotations[i]) - ord('A')) % 26 + ord('A')) for i, c in enumerate(new_msg)]
print(''.join(final_msg))