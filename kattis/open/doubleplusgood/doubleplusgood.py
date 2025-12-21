from itertools import product

def evaluate_expression(expression, operations):
    i = 0
    while i < len(operations): # concats
        if operations[i] == '*':
            expression[i] = int(str(expression[i]) + str(expression[i + 1]))
            expression.pop(i + 1)
            operations.pop(i)
        else:
            i += 1

    result = expression[0]
    for i in range(1, len(expression)): # adds
        result += expression[i]

    return result



parts = input().split('+')
nums = [int(part) for part in parts]
n = len(nums) - 1


operations_combinations = product(['+', '*'], repeat=n) # all combinations

results = set()
for ops in operations_combinations:
    expr_copy = nums.copy()
    result = evaluate_expression(expr_copy, list(ops))
    results.add(result)

print(len(results))