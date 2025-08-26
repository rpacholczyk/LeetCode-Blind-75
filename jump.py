class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_number_to_reach = 0
        for current_index,jump_length  in enumerate(nums):
            if maximum_number_to_reach<current_index:
                return False
            maximum_number_to_reach = max(maximum_number_to_reach,current_index+jump_length)
        return True
