class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        for n in nums:
            if n in dt.keys():
                dt[n] += 1
            else:
                dt[n] = 1
        srr = sorted(dt.keys(), key=lambda kk: dt[kk], reverse=True)
        to_ret = []
        for i in range(k):
            to_ret.append(srr[i])
        return to_ret