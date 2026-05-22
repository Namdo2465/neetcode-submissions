class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            subset = []
            j = 0
            while j < k:
                subset.append(nums[i+j])
                j += 1
            res.append(max(subset))
        return res
