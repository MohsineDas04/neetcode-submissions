class Solution:
    def trap(self, bars: List[int]) -> int:
        width = len(bars)
        s = 0
        for i in range(width):
            s += max(min([max(bars[:i]+[0]), max(bars[i:]+[0])]) - bars[i],0)
        return s
