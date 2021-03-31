n = 5

# Work with recursion

def recursion_function(n):
    if n > 0:
        recursion_function(n - 1)
        print(n)

print(recursion_function(n))

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(n))

# Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# print(fibonacci(n))

# for i in range(n):
#     print(fibonacci(i), end=" ")
# print()
