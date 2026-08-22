class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        i = 0
        res = 0
        for j in range(len(s)):
            seen[s[j]] += 1
            while seen[s[j]] > 1:
                seen[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
            

