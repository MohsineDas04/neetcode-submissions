class Solution:
    def trap(self, bars: List[int]) -> int:
        # mx = max(bars)
        # n = len(bars)
        # res = 0
        # for i in range(len(bars) - 1):
        #     if bars[i] == 0 and i != 0:
        #         j = 1
        #         while ((0 <= i - j < n) and (0 <= i + j < n)):
        #             l = bars[i - j]
        #             r = bars[i + j]

        #             print(f"checking left: {l} and right: {r}")

        #             if l < mx and r < mx:
        #                 res += (mx - l)
        #                 res += (mx - r)
        #                 j += 1
        #             else:
        #                 if l < mx or r < mx:
        #                     res += min([l , r])
        #                 else:
        #                     res += mx
        #                 print(f"stopping at {l , r}")
        #                 break
        # return res
        # height = max(bars)
        width = len(bars)
        
        s = 0

        for i in range(width):
            s += max(min([max(bars[:i]+[0]), max(bars[i:]+[0])]) - bars[i],0)

        return s
