# LeetCode 566: Reshape the Matrix
# Time Complexity: O(m*n), Space Complexity: O(m*n)

class Solution:
    def matrixReshape(self, mat, r, c):
        flat = [num for row in mat for num in row]
        if r * c != len(flat):
            return mat
        new_matrix = []
        for i in range(0, len(flat), c):
            new_matrix.append(flat[i:i + c])
        return new_matrix
