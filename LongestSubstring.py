class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        how_long_is_the_str = len(s)
        resolution = 0
        last_index = [-1] * 26
        start_index = 0
        for end in range(how_long_is_the_str):
            start_index = max(start_index,last_index[ord(s[end]) - ord('a')]+1)
            resolution = max(resolution,end-start_index+1)
            last_index[ord(s[end]) - ord('a')] = end
        return resolution
