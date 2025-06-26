class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in range(len(nums)):
            for second_number in range(number+1,len(nums)):
                if nums[number] + nums[second_number] == target:
                    return[number,second_number]
        return []
