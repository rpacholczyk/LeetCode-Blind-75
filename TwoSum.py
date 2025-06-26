class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for position in range(len(nums)):
            for second_position in range(position+1,len(nums)):
                if nums[position] + nums[second_position] == target:
                    return[position,second_position]
        return []
