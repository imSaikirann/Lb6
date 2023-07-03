def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
num = 5
fact = factorial(num)
if fact is None:
    print("Factorial is undefined for negative numbers.")
else:
    print(f"The factorial of {num} is {fact}.")
