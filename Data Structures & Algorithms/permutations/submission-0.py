class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, numSet):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in numSet:
                    continue
                path.append(num)
                numSet.add(num)
                backtrack(path, numSet)
                removed = path.pop()
                numSet.remove(removed)
        backtrack([], set())
        return res