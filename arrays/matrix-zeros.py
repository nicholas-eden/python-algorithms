from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return

        m = int(9223372036854775807)

        top_row = matrix[0]
        row_len = len(top_row)
        top_found = False
        for i in range(0, len(top_row)):
            if top_row[i] == 0:
                top_found = True
                break

        for r in range(0, len(matrix)):
            row = matrix[r]
            found = False
            for i in range(len(row)):
                if row[i] == 0:
                    found = True
                    matrix[0][i] = m

            if found and r != 0:
                matrix[r] = [0 for _ in range(len(row))]

        for i in range(0, row_len):
            if top_row[i] == m:
                for row in matrix:
                    row[i] = 0

        if top_found:
            matrix[0] = [0 for _ in range(row_len)]


test = Solution()
data = [[0, 5, 6, 6, 9], [7, 0, 3, 3, 1], [1, -2147483648, 7, 2147483647, 8]]
test.setZeroes(data)
print(data)
