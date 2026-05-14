class Solution:
    def trap(self, bars: List[int]) -> int:
        s = 0
        for i in range(len(bars)):
            s += max(min([max(bars[:i]+[0]), max(bars[i:]+[0])]) - bars[i],0)
        return s
