class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sor = sorted(list(set(nums)))
        curr = 1
        highest = 1
        print(sor)
        sp = set()
        for i in range(len(sor) - 1):
            print(f"checking {sor[i]} with {sor[i + 1]}")
            if sor[i + 1] - sor[i] == 1:
                sp.add(sor[i])
                sp.add(sor[i + 1]) 
                curr += 1
            else:
                if i != len(sor) - 2:
                    sp = set()
                if curr > highest:
                    highest = curr
                curr = 1
        return max([len(sp), highest, curr])