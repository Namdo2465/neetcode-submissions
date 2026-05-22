from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        count_list = []
        for num in num_count:
            count_list.append(num_count[num])
        count_list.sort(reverse=True)
        output = []

        used_set = set()
        for i in range(k):
            for num in nums:
                if (num not in used_set):
                    if (num_count[num] == count_list[i]):
                        output.append(num)
                        used_set.add(num)
        return output
