class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The maximum sum found so far
        total_sum = nums[0]
         # The maximum sum found so far for the subarray
        total_sum_subarray = nums[0]
        for num in range(1,len(nums)):
            # Either extend the previous subarray or start a new one from the current element
            total_sum_subarray = max(total_sum_subarray+nums[num],nums[num])
            # Update result if the new subarray sum is larger
            total_sum = max(total_sum,total_sum_subarray)
        return total_sum
