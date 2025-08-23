n = int(input("Enter the number of elements in array: "))
target = int(input("Enter the target sum: "))
arr = []
for i in range(n):
    element = int(input("Enter the element for array: "))
    arr.append(element)
print(arr)
for j in range(n):
    for k in range(n):
        if arr[j] + arr[k] == target:
            print("Combination is " , j , "and " , k , "elements.")
        