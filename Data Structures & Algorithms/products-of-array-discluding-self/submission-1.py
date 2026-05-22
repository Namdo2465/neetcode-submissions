import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = math.prod(nums)
        index_dict = {}
        prod = 1
        for i,num in enumerate(nums):
            index_dict[i] = num
        clone_dict = index_dict
        res = []
        for i in range(len(nums)):
            if index_dict[i] != 0:
                res.append(int(total_product/index_dict[i]))
            else:
                for j in range((len(nums))):
                    if j != i:
                        prod *= index_dict[j]
                res.append(prod)
        return res