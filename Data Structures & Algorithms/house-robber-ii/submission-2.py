class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n1 = len(nums)
        if n1 == 1:
            return nums[0]
        if n1 == 2:
            return max(nums)
        def dfs(nums):
            n2 = len(nums)
            if n2 <= 2:
                return max(nums)
            max_money = [0]*n2
            max_money[0] = nums[0]
            max_money[1] = max(nums[0], nums[1])
            for i in range(2, n2):
                max_money[i] = max((max_money[i-2] + nums[i]), max_money[i-1])
            return max_money[-1]
        return max(dfs(nums[1:]), dfs(nums[0:(len(nums)-1)]))
        
        