# LeetCode 485: Max Consecutive Ones
# Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
