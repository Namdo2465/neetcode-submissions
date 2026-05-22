class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 1
            current_temp = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > current_temp:
                    break
                else:
                    count += 1
                    j += 1
            if j == len(temperatures):
                res.append(0)
            else:
                res.append(count)
        return res
