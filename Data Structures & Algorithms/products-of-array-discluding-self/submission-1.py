from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = {0: nums[0 + 1:]}
        for i in range(1,len(nums)):
            results[i] = nums[i + 1:] + nums[:i]
        return [prod(val) for k, val in results.items()]