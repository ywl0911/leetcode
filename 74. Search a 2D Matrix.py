class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        row = m - 1
        column = 0
        while row >= 0 and column < n:
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                row -= 1
            else:
                column += 1

        return False
