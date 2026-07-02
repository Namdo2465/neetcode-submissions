class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_list = list(set(nums))
        unique_list.sort()
        if unique_list == []:
            return 0
        else:
            res = 1
            i = 0
            while i < len(unique_list):
                j = i
                while j < len(unique_list) - 1 and unique_list[j] + 1 == unique_list[j+1]:
                    j += 1
                res = max(res, j - i + 1)
                i = j + 1
        return res
            