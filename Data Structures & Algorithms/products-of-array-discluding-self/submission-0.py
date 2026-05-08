class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        results = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                result = result * nums[j]
            results.append(result)
            result = 0
        return results