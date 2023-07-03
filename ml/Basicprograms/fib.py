def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Example usage
num_terms = 10
fib_sequence = fibonacci_sequence(num_terms)
print(fib_sequence)
