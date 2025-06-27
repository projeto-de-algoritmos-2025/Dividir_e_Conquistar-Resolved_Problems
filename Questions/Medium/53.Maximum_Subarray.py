from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            max_left = helper(left, mid)
            max_right = helper(mid + 1, right)

            left_sum = float('-inf')
            total = 0
            for i in range(mid, left - 1, -1):
                total += nums[i]
                left_sum = max(left_sum, total)

            right_sum = float('-inf')
            total = 0
            for i in range(mid + 1, right + 1):
                total += nums[i]
                right_sum = max(right_sum, total)

            max_cross = left_sum + right_sum

            return max(max_left, max_right, max_cross)

        return helper(0, len(nums) - 1)
