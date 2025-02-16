
# DSA: W3Schools - Main Tutorial
# Section 2: Simple Algorithm Example

# Fibonacci using iteration:
def fibonacci_iteration(n):
    prev1 = 0
    prev2 = 1

    for _ in range(n):
        newFibo = prev1 + prev2
        prev1 = prev2
        prev2 = newFibo
    return prev1

for i in range(10):
    print(fibonacci_iteration(i))

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

for i in range(10):
    print(fibonacci_recursion(i))
