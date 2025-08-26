class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_counts = [1] * n
        for row in range(1,m):
            for col in range(1,n):
                path_counts[col]+=path_counts[col-1]
        return path_counts[-1]
