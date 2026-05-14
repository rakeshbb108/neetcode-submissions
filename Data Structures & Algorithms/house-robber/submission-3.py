class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)
        prev0 = nums[0]
        prev1 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            cur = max(nums[i]+prev0, prev1)
            prev0 = prev1
            prev1 = cur
        return prev1