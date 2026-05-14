class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        poss = sorted(list(filter(lambda n: n >= 0, nums)))

        print(poss)
        for n in range(1, max(nums) + 1):
            if n not in poss:
                return n
            elif n + 1 not in poss:
                return n + 1
        return 1