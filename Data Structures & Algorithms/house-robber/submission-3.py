class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        max_sum = [0]*(n)
        max_sum[0] = nums[0]
        max_sum[1] = nums[1]
        for i in range(2, n):
            max_sum[i] = max(max_sum[0:i-1]) + nums[i]
        return max(max_sum[n-1], max_sum[n-2])
