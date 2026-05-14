class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        prev0 = nums[0]
        prev1 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            cur = max(nums[i]+prev0, prev1)
            prev0 = prev1
            prev1 = cur
        return max(prev0,prev1)