class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            hashMap[n] = i
        for i, n in enumerate(nums):
            complement = target-n
            if complement in hashMap and i != hashMap[complement]:
                return [i, hashMap[complement]]
        return []
        