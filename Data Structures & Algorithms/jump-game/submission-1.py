class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0]
        for i in range(len(nums)):
            if max_reach >= len(nums) - 1:
                return True
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        
        return max_reach >= len(nums) - 1
            