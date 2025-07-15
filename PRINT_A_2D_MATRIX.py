# DSA Task: Print a 2D Matrix

n = int(input("Enter number of rows for Matrix A: "))
m = int(input("Enter number of columns for Matrix A: "))

matrix1 = []
print("\nEnter elements for Matrix A:")
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

print("\nMatrix A:")
for row in matrix1:
    print(row)
