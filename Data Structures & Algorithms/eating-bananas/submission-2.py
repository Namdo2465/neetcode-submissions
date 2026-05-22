import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = float('inf')
        lower = 1
        upper = max(piles) 
        while lower <= upper:
            middle = (lower + upper) // 2
            total_hour = 0
            for bananas in piles:
                total_hour += math.ceil(bananas / middle)
                if total_hour > h:
                    lower = middle + 1
                    break
            if total_hour <= h:
                ans = min(ans,middle)
                upper = middle - 1
                print(ans,lower,upper)

        return ans