class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][j] , new_interval[0]:
            res.append(intervals[i])
            i+=1
        while i < n and new_interval[1] >= intervals[i][0]:
            new_interval[0] = min(new_interval[0],intervals[i][o])
            new_interval[1] = max(new_interval[1],intervals[i][1])
            i+=1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i+1
        return res
        
