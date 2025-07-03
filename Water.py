class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_height = len(height)
        resolution = 0
        for numb in range(len_height):
            for sec_num in range(numb+1,len_height):
                water_amount = min(height[numb],height[sec_num]) * (sec_num - numb)
                resolution = max(water_amount,resolution)
        return resolution


        
