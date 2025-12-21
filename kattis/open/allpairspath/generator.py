import random

def generate_test_case(num_nodes, num_edges, num_queries):
    test_case = []

    # Add the first line with num_nodes, num_edges, num_queries
    test_case.append(f"{num_nodes} {num_edges} {num_queries}")

    # Generate random edges
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        w = random.randint(1, 100)  # Assuming weights are between 1 and 100
        test_case.append(f"{u} {v} {w}")

    # Generate random queries
    for _ in range(num_queries):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        test_case.append(f"{u} {v}")

    return "\n".join(test_case)

def generate_input(num_test_cases, max_nodes, max_edges, max_queries):
    input_data = []

    for _ in range(num_test_cases):
        num_nodes = random.randint(1, max_nodes)
        num_edges = random.randint(0, min(max_edges, num_nodes * (num_nodes - 1)))
        num_queries = random.randint(1, max_queries)
        input_data.append(generate_test_case(num_nodes, num_edges, num_queries))

    return "\n\n".join(input_data)

# Example usage
if __name__ == "__main__":
    num_test_cases = 5
    max_nodes = 10
    max_edges = 20
    max_queries = 5

    input_data = generate_input(num_test_cases, max_nodes, max_edges, max_queries)
    print(input_data)