class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for item in range(len(matrix)):
            for second_item in range(item,len(matrix[0])):
                matrix[item][second_item],matrix[second_item][item] = matrix[second_item][item], matrix[item][second_item]
        for row in matrix:
            row.reverse()
