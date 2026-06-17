class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        if s == "":
            return cnt
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                left = i
                right = i+1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
        return cnt
            
        