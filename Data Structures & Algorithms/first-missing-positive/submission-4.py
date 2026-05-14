class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for n in range(1, max(nums) + 1):
            if n not in nums:
                return n
            elif n + 1 not in nums:
                return n + 1
        return 1