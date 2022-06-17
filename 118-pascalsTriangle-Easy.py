class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for x in range(numRows):
            row = [None for i in range(x+1)]
            row[0], row[-1] = 1, 1
            #row[-1] = 1
            for y in range(1, x):
                row[y] = triangle[x-1][y-1] + triangle[x-1][y]
            triangle.append(row)
        return triangle
