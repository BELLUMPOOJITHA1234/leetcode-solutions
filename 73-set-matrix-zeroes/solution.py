// 7 ms | 20.9 MB
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all rows and columns containing 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Make those rows zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Make those columns zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0