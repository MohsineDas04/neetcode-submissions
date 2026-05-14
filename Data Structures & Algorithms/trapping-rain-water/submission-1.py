class Solution:
    def trap(self, bars: List[int]) -> int:
        width = len(bars)
        height = max(bars)
        matrix = [[0] * width for i in range(height)]  
        for i in range(height):
            for j in range(width):
                matrix[i][j] = 1 if i < bars[j] else 0
        s = 0
        for i in range(height):
            row = matrix[i]
            for j in range(width):
                if matrix[i][j] == 1:
                    continue
                if 1 in row[:j] and 1 in row[j:]:
                    s += 1

        return s