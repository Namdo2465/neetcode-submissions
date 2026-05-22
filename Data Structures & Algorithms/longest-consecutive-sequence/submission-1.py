class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_list = list(set(nums))
        unique_list.sort()
        if unique_list == []:
            return 0
        else:
            res, i = 1, 0
            output_set = set()
            while i < len(unique_list) - 1:
                if unique_list[i+1] - unique_list[i] == 1:
                    res += 1
                    i += 1
                else:
                    output_set.add(res)
                    res = 1
                    i += 1
            output_set.add(res)
            output = max(output_set)
            return output