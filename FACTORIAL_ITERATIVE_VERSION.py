def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter the number whose factorial you want: "))
print("Factorial (Recursive):", factorial(n))
print("Factorial (Iterative):", factorial_iterative(n))
