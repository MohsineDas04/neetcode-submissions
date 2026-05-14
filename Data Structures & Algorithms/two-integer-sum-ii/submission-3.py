class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            print(f"outside i is: {i}")
            for j in range(i + 1, len(numbers)):
                print(f"inside j is: {j}")
                print(f"summing {numbers[i]} + {numbers[j]}")
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []