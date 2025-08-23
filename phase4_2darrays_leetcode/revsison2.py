# Problem 1 – 2nd Largest Element
arr1 = [7, 1, 5, 3, 6, 4]
arr1.sort()
print("2nd max element is:", arr1[-2])  # 6


# Problem 2 – Rotate Array by K
arr2 = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr2)  # handle if k > n
rotated = arr2[-k:] + arr2[:-k]
print("Rotated array:", rotated)  # [5, 6, 7, 1, 2, 3, 4]


# Problem 3 – Move Zeroes to End
arr3 = [0, 1, 0, 3, 12]
result = [x for x in arr3 if x != 0]  # keep only non-zeros
result += [0] * (len(arr3) - len(result))  # add zeros at end
print("After moving zeroes:", result)  # [1, 3, 12, 0, 0]


# Problem 4 – Find Unique Element
arr4 = [2, 3, 5, 4, 5, 3, 2]
for num in arr4:
    if arr4.count(num) == 1:
        print("Unique element is:", num)  # 4
        break


# Problem 5 – Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

print("Is arr [1,3,2,4,5] sorted?", is_sorted([1, 3, 2, 4, 5]))  # False
print("Is arr [1,2,3,4,5] sorted?", is_sorted([1, 2, 3, 4, 5]))  # True
