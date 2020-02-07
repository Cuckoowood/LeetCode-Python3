class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        n_row = len(matrix)  # ����
        n_col = len(matrix[0])  # ����
        row, col = n_row - 1, 0  # ��ʼ�������½�
        while row >= 0 and col < n_col:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
